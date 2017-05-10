# -*- coding: utf-8 -*-
# Copyright 2016 Serpent Consulting Services Pvt. Ltd.
# See LICENSE file for full copyright and licensing details.

from odoo.tests import common


class ProjectTestCase(common.TransactionCase):
    def setup(self):
        super(ProjectTestCase, self).setup()

    def test_project_kanban(self):
        self.project_obj = self.env['project.project']
        self.record = self.project_obj.\
            create({'name': 'Project Kanban',
                    'recent_date': self.project_obj._get_recent_date()})
