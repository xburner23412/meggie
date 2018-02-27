# coding: utf-8


"""
Created on Oct 22, 2013
@author: Janne Pesonen, Kari Aliranta

Classes needed for controlling Meggie experiments.

"""
import os
import re
import json
import shutil
import logging

from meggie.ui.utils.decorators import threaded

from meggie.code_meggie.general.caller import Caller
from meggie.code_meggie.general import fileManager
from meggie.code_meggie.general.subject import Subject
from meggie.code_meggie.epoching.epochs import Epochs
from meggie.code_meggie.epoching.evoked import Evoked

from PyQt4.QtCore import QObject


class Experiment(QObject):
    
    """A class that holds experiment info.

    Experiment stores path of the experiment file, author, description and
    list of the subjects. It also has methods for saving and parsing parameter
    files and pickling and unpickling itself to and from disk.

    Properties:
    experiment_name    -- The name of the experiment
    workspace          -- The path to the experiment folder
    author             -- The name of the experiment's author
    description        -- A user defined description of the experiment
    subjects           -- The list of the Subject objects in this experiment
    active_subject     -- The subject that is currently processed
    """
    caller = Caller.Instance()


    def __init__(self):
        """
        Constructor sets default values for attributes.
        """
        QObject.__init__(self)
        self._experiment_name = 'experiment'
        self._author = 'unknown author'
        self._description = 'no description'
        self._subjects = {}
        self._active_subject = None
        self._workspace = None
        self._layout = 'Infer from data'

        

    @property
    def workspace(self):
        return self._workspace
    
    @workspace.setter
    def workspace(self, workspace):
        self._workspace = workspace

    @property
    def experiment_name(self):
        """
        Returns the name of the experiment.
        """
        return self._experiment_name

    @experiment_name.setter
    def experiment_name(self, experiment_name):
        """
        Sets the name for the experiment. 
        Keyword arguments:
        experiment_name    -- the name of the experiment
        """
        name = os.path.basename(experiment_name)
        
        if (len(name) <= 30):
            if re.match("^[A-Za-z0-9_ ]*$", name):
                self._experiment_name = str(experiment_name)
            else:
                raise ValueError('Use only letters and numbers in experiment' +
                                 'name')
        else:
            raise ValueError('Too long experiment name')

    @property
    def author(self):
        """
        Returns the author of the experiment
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of the experiment.
        Raises exception if the author name is too long.
        Raises exception if the author name includes other characters
        than letters and numbers.
        Keyword arguments:
        author          - - the author of the experiment
        """
        if (len(author) <= 30):
            if re.match("^[A-Za-zäÄöÖåÅ0-9 ]*$", author):
                self._author = author
            else:
                raise ValueError("Use only letters and numbers in _author name")
        else:
            raise ValueError('Too long _author name')

    @property
    def description(self):
        """
        Returns the _description of the experiment.
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the _description of the experiment written by the _author.
        Raises exception if the _description is too long.
        Raises exception if the _description includes other characters
        than letters and numbers.        
        Keyword arguments:
        description     -- the description of the experiment written by the
                           author
        """
        if (len(description) <= 1000):
            if (re.match(
                "^[A-Za-zäÄöÖåÅ0-9 \t\r\n\v\f\]\[!\"#$%&'()*+,./:;<=>?@\^_`{|}~-]+$",
                 description) or len(description) == 0):
                self._description = description
            else:
                raise ValueError("Use only letters and " + 
                                 "numbers in your _description")
        else:
            raise ValueError("Too long _description")

    @property
    def layout(self):
        return self._layout
    
    @layout.setter
    def layout(self, layout):
        self._layout = layout

    @property
    def active_subject(self):
        """
        Method for getting activated subject.
        """
        return self._active_subject

    @active_subject.setter
    def active_subject(self, subject):
        """
        Method for setting active subject.
        """
        self._active_subject = subject

    def add_subject(self, subject):
        """
        Adds subject to the current experiment.
        
        Keyword arguments:
        subject    -- the subject object created by subject class
        """
        self.subjects[subject.subject_name] = subject

    @property
    def subjects(self):
        """
        Returns a dict of all subjects.
        """
        return self._subjects

    def remove_subject(self, sname, main_window):
        """
        Removes the subject folder and its contents under experiment tree.
        Removes the subject information from experiment properties and updates
        the experiment settings file.

        Keyword arguments:
        sname        -- name of the subject to remove
        main_window -- MainWindow object
        """
        
        if getattr(self, 'active_subject', None) and self.active_subject.subject_name == sname:
            self.active_subject = None
        
        subject = self.subjects.pop(sname)
    
        @threaded
        def remove_data(): 
            try:
                shutil.rmtree(subject.subject_path)
            except OSError:
                raise OSError('Could not remove the contents of the subject folder.')    
        
        remove_data()

    def activate_subject(self, subject_name):
        """Activates a subject from the existing subjects

        Keyword arguments:
        subject_name -- name of the subject
        """
        # Remove raw files from memory before activating new subject.
        if self.active_subject:
            self.active_subject.release_memory()

        self.active_subject = self.subjects[subject_name]
        return self.active_subject
 
    @threaded
    def create_subject(self, subject_name, experiment, working_file_name, raw_path=None):
        """Creates a Subject when adding a new one to the experiment.
        
        Keyword arguments:
        subject_name    -- name of the subject
        experiment      -- Experiment object
        """
        subject = Subject(experiment, subject_name, working_file_name)
        if raw_path:
            fileManager.save_subject(subject, raw_path)
        self.add_subject(subject)


    def save_experiment_settings(self):
        """
        Saves the experiment settings into a file in the root of
        the experiment directory structure.
        """        
        subjects = []

        for subject in self.subjects.values():
            subject_dict = {
                'subject_name': subject.subject_name,
                'working_file_name': subject.working_file_name,
                'epochs': [], 
                'evokeds': [],
            }
            for epoch in subject.epochs.values():
                epoch_dict = {
                    'collection_name': epoch.collection_name,
                    'params': epoch.params
                }
                subject_dict['epochs'].append(epoch_dict)
            for evoked in subject.evokeds.values():
                try:
                    evoked_dict = {
                        'name': evoked.name,
                        'event_names': evoked.mne_evokeds.keys(),
                        'info': evoked.info,
                    }
                    subject_dict['evokeds'].append(evoked_dict)
                except IOError:
                    del subject.evokeds[evoked.name]
                    message = 'Missing evoked response file. Experiment updated.'
                    logging.getLogger('ui_logger').warning(message)
            subjects.append(subject_dict)
        
        save_dict = {
            'subjects': subjects,
            'name': self.experiment_name,
            #'workspace': self.workspace,
            'author': self.author,
            'description': self.description,
            'layout': self.layout,
        }

        version = ''
        try:
            import pkg_resources
            version = pkg_resources.get_distribution("meggie").version
        except:
            pass

        save_dict['version'] = version

        try:
            os.makedirs(os.path.join(self.workspace, self.experiment_name))
        except OSError:
            pass
        
        # save to file
        with open(os.path.join(self.workspace, self.experiment_name, self.experiment_name + '.exp'), 'w') as f:  # noqa
            json.dump(save_dict, f, sort_keys=True, indent=4)
            
        if self.caller.experiment: 
            self.caller.parent.initialize_ui()


class ExperimentHandler(QObject):
    """
    Class for handling the creation of a new experiment.
    
    TODO: should also handle switching active experiment.
    """
    
    def __init__(self, parent):
        """
        Constructor
        Keyword arguments:
        parent        -- Parent of this object.
        """
        self.parent = parent

    def initialize_new_experiment(self, expDict):
        """
        Initializes the experiment object with the given data. Assumes that
        Meggie is currently devoid of a current experiment.
        
        TODO: Keyword arguments:
           
        """
        prefs = self.parent.preferencesHandler
      
        try:
            experiment = Experiment()
            experiment.author = expDict['author']
            experiment.experiment_name = os.path.basename(expDict['name'])
            #experiment.experiment_name = expDict['name']
            experiment.description = expDict['description']
        except AttributeError:
            raise Exception('Cannot assign attribute to experiment.')
        
        experiment.workspace = prefs.working_directory
        #experiment.workspace = os.path.join(prefs.working_directory, expDict['name'])
        
        experiment.save_experiment_settings()
        
        prefs.previous_experiment_name = os.path.join(experiment.workspace, experiment.experiment_name)
        prefs.write_preferences_to_disk()
        
        return experiment

    def open_existing_experiment(self, prefs, path=None):
        """
        Opens an existing experiment, which is assumed to be in the working
        directory.
        
        Keyword arguments:
        
        name        -- name of the existing experiment to be opened
        """
        
        if path:
            exp_file = os.path.join(path, os.path.basename(path) + '.exp') 
        else:
            if prefs.previous_experiment_name == '':
                return
            exp_file = os.path.join(
            prefs.previous_experiment_name,
            os.path.basename(prefs.previous_experiment_name) + '.exp'
            )
        
        if not os.path.isfile(exp_file):
            raise ValueError('Trying to open experiment without settings file (.exp).')
        
        try:
            with open(exp_file, 'r') as f:
                data = json.load(f)
        except ValueError:
            raise ValueError('Experiment from ' + exp_file + ' could not be ' + 
                             'opened. If it is an old experiment, you might ' + 
                             'want to create a new one as old-style ' + 
                             '(pre 0.1.5) experiments are not supported ' + 
                             'anymore.')
            
        prefs = self.parent.preferencesHandler
        experiment = Experiment()
        experiment.author = data['author']
        experiment.experiment_name = data['name']
        experiment.description = data['description']
        
        if 'layout' in data.keys():
            experiment.layout = data['layout']
        else:
            experiment.layout = 'Infer from data'
        
        if path:
            experiment.workspace = os.path.dirname(path)
        else:
            experiment.workspace = os.path.dirname(
                prefs.previous_experiment_name)
        
        if len(data['subjects']) > 0:
                
            for subject_data in data['subjects']:
                
                subject = Subject(experiment, subject_data['subject_name'],
                                  subject_data['working_file_name'])
                
                for epoch_data in subject_data['epochs']:
                    epochs = Epochs(epoch_data['collection_name'], subject,
                        epoch_data['params'])
                    epochs.collection_name = epoch_data['collection_name']
                    epochs.params = epoch_data['params']
                    subject.add_epochs(epochs)
                
                for evoked_data in subject_data['evokeds']:
                    mne_evokeds = dict([(name, None) for name in evoked_data['event_names']])
                    evoked = Evoked(evoked_data['name'], subject, mne_evokeds)
                    if 'info' in evoked_data:
                        evoked.info = evoked_data['info']
                    subject.add_evoked(evoked)
                experiment.add_subject(subject)

        prefs.previous_experiment_name = os.path.join(experiment.workspace, experiment.experiment_name)

        return experiment
