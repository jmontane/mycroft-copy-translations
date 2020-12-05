#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# Copyright (c) 2020 Joan Montané <jmontane@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import os
import shutil

MYCROFT_SKILLS_DIR = '/opt/mycroft/skills'
MYCROFT_SOURCE_LOCALE = 'ca'
MYCROFT_TARGET_LOCALE = 'ca-es'

def get_list_of_skills(path):
   return [f.path for f in os.scandir(path) if f.is_dir()]

def is_locale_skill(skill):
    return os.path.isdir(skill + '/locale')

def move_locale_skill(path):

    if os.path.isdir(path + MYCROFT_SOURCE_LOCALE):
         # if target locale directory exists...
         if os.path.isdir(path + MYCROFT_TARGET_LOCALE):
              # remove old backup...
              if os.path.isdir(path + MYCROFT_TARGET_LOCALE + '_backup'):
                  shutil.rmtree(path + MYCROFT_TARGET_LOCALE + '_backup')
              # create new backup...
              shutil.copytree(path + MYCROFT_TARGET_LOCALE,
                        path + MYCROFT_TARGET_LOCALE + '_backup')
              # remove target locale directory...
              shutil.rmtree(path + MYCROFT_TARGET_LOCALE)

         # and copy source locale to target locale directory	
         shutil.copytree(path + MYCROFT_SOURCE_LOCALE,
                   path + MYCROFT_TARGET_LOCALE)
    return


List_of_skills = get_list_of_skills(MYCROFT_SKILLS_DIR)


for skill in List_of_skills:
    print('Working on ' + skill)
    if (is_locale_skill(skill)):
        move_locale_skill(skill + '/locale/')
    else:
       print('It\'s a non-locale skill')
       for subdir in ['/dialog/', '/vocab/', '/regex/']:
           move_locale_skill(skill + subdir)
