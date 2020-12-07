#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
#
# MIT License
# 
# Copyright (c) 2020 Joan Montané
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE
.
import os
import shutil

MYCROFT_SKILLS_DIR = '/opt/mycroft/skills'
MYCROFT_SOURCE_LOCALE = 'ca'
MYCROFT_TARGET_LOCALE = 'ca-es'

def get_list_of_skills(path):
   return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

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
