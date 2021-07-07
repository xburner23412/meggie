""" Contains a class for logic of pipeline dialog.
"""

import os
import json
import logging
import pkg_resources

from PyQt5 import QtWidgets

from meggie.mainwindow.dynamic import find_all_sources

from meggie.mainwindow.dialogs.pipelineDialogUi import Ui_pipelineDialog

from meggie.utilities.messaging import messagebox


class PipelineDialog(QtWidgets.QDialog):
    """ Contains logic for preferences dialog.
    """

    def __init__(self, parent, prefs):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_pipelineDialog()
        self.ui.setupUi(self)

        self.parent = parent
        self.experiment = parent.experiment

        # Read selected pipeline from the experiment
        selected_pipeline = self.experiment.selected_pipeline

        self.active_plugins = prefs.active_plugins

        # read all pipeline ids and names to a list
        pipelines = []
        sources = find_all_sources()
        for source in sources:
            if source == 'meggie' or source in self.active_plugins:
                config_path = pkg_resources.resource_filename(
                    source, 'configuration.json')
                with open(config_path, 'r') as f:
                    config = json.load(f)
                if 'pipelines' in config:
                    for pipeline in config['pipelines']:
                        try:
                            id_ = pipeline['id']
                        except Exception as exc:
                            raise Exception('Every pipeline should have id.')

                        name = pipeline.get('name', '')
                        pipelines.append((id_, name))

        # remove possible duplicates and hope that the first has the name
        self.pipelines = []
        for pipeline in pipelines:
            if pipeline[0] not in [pipe[0] for pipe in self.pipelines]:
                if pipeline[1]:
                    self.pipelines.append(pipeline)
                else:
                    self.pipelines.append((pipeline[0], pipeline[0]))

        # create buttons for pipelines
        self.pipeline_buttons = []
        for idx, (pipeline_id, pipeline_name) in enumerate(self.pipelines):
            radio_button = QtWidgets.QRadioButton(self.ui.groupBoxPipeline)
            radio_button.setText(pipeline_name)

            self.ui.gridLayoutPipeline.addWidget(
                radio_button, idx + 1, 0, 1, 1)

            self.pipeline_buttons.append(radio_button)

            if selected_pipeline == pipeline_id:
                radio_button.setChecked(True)

        if len(self.pipeline_buttons) == 1:
            self.pipeline_buttons[0].setEnabled(False)
            self.pipeline_buttons[0].setChecked(True)

    def accept(self):

        selected_pipeline = ""
        for button_idx, radio_button in enumerate(self.pipeline_buttons):
            if radio_button.isChecked():
                selected_pipeline = self.pipelines[button_idx][0]
                break

        # store selected pipeline to the experiment
        if selected_pipeline:
            self.experiment.selected_pipeline = selected_pipeline
            self.experiment.save_experiment_settings()
            self.parent.reconstruct_tabs()
            self.parent.initialize_ui()

        self.close()
