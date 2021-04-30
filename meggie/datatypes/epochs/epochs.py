# coding: utf-8

"""
"""
import os
import logging

import mne

from meggie.utilities.datatype import Datatype


class Epochs(Datatype):
    """
    """

    def __init__(self, name, epochs_directory, params, content=None):
        """
        """
        self._name = name
        self._content = content
        self._params = params
        self._path = os.path.join(epochs_directory, name + '.fif')

    @property
    def content(self):
        """
        """
        if self._content is not None:
            return self._content
        else:
            try:
                self._content = mne.read_epochs(self._path)
                return self._content
            except IOError:
                raise Exception('Reading epochs failed.')

    @property
    def name(self):
        """
        """
        return self._name

    @property
    def count(self):
        """
        """
        return len(self.content.events)

    @property
    def params(self):
        """
        """
        return self._params

    @property
    def path(self):
        return self._path

    def delete_content(self):
        os.remove(self._path)

    def save_content(self):
        try:
            self._content.save(self._path, overwrite=True)
        except Exception as exc:
            logging.getLogger('ui_logger').exception('')
            raise IOError('Writing epochs failed')
