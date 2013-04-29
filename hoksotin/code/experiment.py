"""
Created on Mar 6, 2013

@_author: Janne Pesonen
"""

import mne

import os

import time
import re
import csv


import numpy as np

# Better to use pickle rather than cpickle, as experiment paths may
# include unicode characters
import pickle

from node import Node
from tree import Tree

class Experiment(object):
    """
    Experiment holds information about the currently saved raw data,
    path of the experiment file, _author, date and _description.
    """
    
    def __init__(self):
        """
        Constructor sets default values for attributes.
        """
        
        self._experiment_name = 'experiment'
        self._raw_data = 'no data specified'
        self._subject_directory = 'no directory specified'
        self._file_path = 'no path defined'
        self._author = 'unknown _author'
        self._description = 'no _description'
        self.date = time.strftime('%Y %m %d %X')
        self.tree = Tree()
        self.__index = 0
        self._event_set = []
        
        # Add here all the possible actions that you can do to an experiment
        # TODO not in use
        self.stateDict = dict(Maxfilter=False, ECGcomputed=False,
                              ECGapplied=False, EOGcomputed=False,
                              EOGapplied=False, Eventlist=False,
                              Epochs=False, Average=False)
                
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
        if (len(experiment_name) <= 30):
            if re.match("^[A-Za-z0-9 ]*$", experiment_name):
                self._experiment_name = experiment_name
            else:
                raise Exception("Use only letters and numbers in experiment \
                name")
        else:
            raise Exception('Too long experiment name')
    
    @property
    def subject_directory(self):
        """
        Returns the absolute path to the subject directory of the experiment.        
        """
        return self._subject_directory
    
    @subject_directory.setter
    def subject_directory(self, subject_directory):
        """
        Sets the subject directory for the experiment. Should be an absolute
        path. Not setable by user, for internal use only.
        TODO: should probably later be a list of subject directories, if the
        experiment is to include several of them
        """
        
        self._subject_directory = subject_directory
    
    @property
    def file_path(self):
        """
        Returns the path of the current experiment file.
        """
        return self._file_path
    
    @file_path.setter
    def file_path(self, file_path):
        """
        Sets the given path for the experiment file.
        Raises exception if the given path doesn't exist.
        
        Keyword arguments:
        file_path       -- the path of the saved experiment
        """
        if (os.path.isdir(file_path)): 
            self._file_path = file_path
        else:
            raise Exception('No such path')
    
    @property
    def raw_data(self):
        """
        Returns the raw data file of the experiment.
        """
        return self._raw_data
    
    @raw_data.setter
    def raw_data(self, raw_data):
        """
        Sets the raw data file for the experiment.
        Raises exception if the given data type is wrong. 
        
        Keyword arguments:
        raw_data        -- the raw data file of the measured data
        """
        if (isinstance(raw_data, mne.fiff.Raw)):
            self._raw_data = raw_data
        else:
            raise Exception('Wrong data type')
    
    @property
    def author(self):
        """
        Returns the _author of the experiment
        """
        return self._author
    
    @author.setter
    def author(self, author):
        """
        Sets the _author of the experiment.
        Raises exception if the _author name is too long.
        Raises exception if the _author name includes other characters
        than letters and numbers.
        
        Keyword arguments:
        author          - - the _author of the experiment
        """
        if (len(author) <= 50):
            if re.match("^[A-Za-z0-9 ]*$", author):
                self._author = author
            else:
                raise Exception("Use only letters and numbers in _author name")
        else:
            raise Exception('Too long _author name')
    
    def update_state(self, key, value):
       self.stateDict[key] = value
       
       # Parent should always refer to main window, or there will be blood
       self.parent.setup_ui_by_experiment_state()   
        
    """
    for 
    
    if (check_file_existence('sss') \
        or check_file_existence('tsss') \
        or check_file_existence('mc')
       ):
        self.stateDict[Maxfilter] = True  
    """
    """    
    def check_file_existence(self, filetypestring):
        filename = self.file_path() + self.
        
        try:
            with open(filename):
                return True
        except IOError:
            return False
        
    """
    
    
    def get_date(self):
        """
        Returns the saving time and date of the experiment.
        """
        return self.date
    
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
        description     - - the _description of the experiment written
        by the _author
        """
        if (len(description) <= 1000):
            if (re.match(
                "^[A-Za-z0-9 \t\r\n\v\f\]\[!\"#$%&'()*+,./:;<=>?@\^_`{|}~-]+$",
                 description) or len(description) == 0):
                self._description = description
            else:
                raise Exception("Use only letters and " + 
                                "numbers in your _description")
        else:
            raise Exception("Too long _description")
    
    @property
    def event_set(self):
        """
        Returns the events as a tuple, where the first element is the id
        and the second element is the number of the events.
        """
        return self._event_set
    
    def create_event_set(self):
        """
        Creates an event set where the first element is the id
        and the second element is the number of the events.
        Raises type error if the raw_data attribute is not set or
        if the data is not of type mne.fiff.Raw.
        """
        if not isinstance(self._raw_data, mne.fiff.Raw):
            raise TypeError('Not a raw object')
        events = mne.find_events(self._raw_data)
        bins = np.bincount(events[:,2]) #number of events stored in an array
        d = dict()
        for i in set(events[:,2]):
            d[i] = bins[i]
        self._event_set = d
    
    def save_experiment_settings(self):
        """
        Saves (pickes) the experiment settings into a file in the root of
        the experiment directory structure. Please note that loading is done
        in the mainWindow class. 
        """
        
        # String conversion, because shutil doesn't accept QStrings
        settingsFileName = str(self._experiment_name + '.pro')
        
        # Actually a file object
        settingsFile = open(self._file_path + '/' + settingsFileName, 'wb')
        
        # Protocol 2 used because of file object being pickled
        pickle.dump(self, settingsFile, 2)
       
        # Move the file from working directory to 
        #shutil.move(settingsFileName, str(self._file_path))
        
        settingsFile.close()        
    
    def save_experiment(self, workspace):
        """
        Creates the experiment folder.
        
        Keyword arguments:
        workspace    -- workspace for the chosen experiment.
        """
        self._file_path = workspace + '/' + self._experiment_name + '/'
        if os.path.exists(workspace):
            try:
                os.mkdir(self._file_path)
            except OSError:
                print "no rights to save to the chosen path"
        else:
            raise Exception('No such path')
        
    def save_raw(self, file_name):
        """
        Saves the raw data file into the experiment folder.
        
        Keyword arguments:
        file_name      -- the full path and name of the chosen raw data file
        """
        folder_name = file_name.split("_", 1)
        try:
            if os.path.exists(self._file_path + folder_name[0]):
                pass
            else:
                os.mkdir(self._file_path + folder_name[0])
        except OSError:
            print "no rights to save the raw file to the chosen path \
            or bad raw file name"
        
        self.subject_directory = str(self._file_path) + folder_name[0] + '/'
        raw_file_path = str(self._file_path) + folder_name[0] + '/' + file_name
        mne.fiff.Raw.save(self._raw_data, raw_file_path)
        self._raw_data = mne.fiff.Raw(raw_file_path)
            
    def save_parameter_file(self, command, inputfilename, outputfilename, dic):
        """
        Saves the command and parameters related to creation of a certain
        output file to a separate parameter file in csv-format.
        TODO: breaks if dictionary keys of values include commas --> check
        
        An example of the structure of the resulting parameter file:
        
        jn_multimodal01_raw_sss.fif
        jn_multimodal01_raw_sss_ecg_proj.fif 
        mne.preprocessing.compute_proj_eog
        tmin,0.2
        tmax,0.5
        .
        .
        .  
        
        Keyword arguments:
        inputfilename    -- name of the file the command with parameters
                            was executed on
        outputfilename   -- the resulting output file from the command
        command          -- command (as string) used
        dic              -- dictionary including commands
        """
        paramfilename = outputfilename + '.param'
        with open(paramfilename, 'wb') as paramfullname:
            print 'writing param file'
            csvwriter = csv.writer(paramfullname)
            
            csvwriter.writerow([inputfilename])
            csvwriter.writerow([outputfilename])
            csvwriter.writerow([command])
            
            for key, value in dic.items():
                csvwriter.writerow([key, value])
                        
    def write_commands(self, commands, node, parent=''):
        """
        Writes an array of commands in a tree structure.
        Used for creating a batch file.
        TODO not in use
        
        Keyword arguments:
        commands      -- An array of commands
        node          -- Node id
        parent        -- Parent of the node
        """
        if parent == '':
            self.tree.create_node(commands, 'prep'+str(self.__index))
        else:
            self.tree.create_node(commands, node + str(self.__index), parent)
        self.__index += 1
        return self.__index - 1
            
    def get_subtree(self, nid, s=''):
        """
        Returns a set of commands from a subtree.
        TODO not in use
        
        Keyword arguments:
        nid           -- ID of the leaf
        s             -- Helper for recursion
        """
        while nid is not None:
            n = self.tree.get_node(nid)
            s = self.get_subtree(n.bpointer, s)
            s += ''.join(n.name)
            return s
        return ''
    