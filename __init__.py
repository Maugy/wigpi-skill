# Copyright 2022 Åke Forslund
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import openai
import os
from os import listdir, remove as remove_file
from os.path import dirname, isfile

from mycroft.api import DeviceApi
from mycroft.skills.core import MycroftSkill, intent_handler
from adapt.intent import IntentBuilder
import dotenv

config = dotenv.dotenv_values("/home/dmauger/mycroft-core/skills/wigpi-skill.maugy/.env")
openai.api_key = config['OPENAI_API_KEY']

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt = prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text 
    return response 

class Wigpi(FallbackSkill):

    def __init__(self):
        super(Wigpi, self).__init__(name='Wigpi')
        
        # reloading skills will also reset this 'timer', so ideally it should
        # not be too high
        # self.line_count = 1
        # self.save_loop_threshold = int(self.settings.get('save_loop_threshold',
        #                                                  4))


    # def initialize(self):
    #     self.register_fallback(self.handle_fallback, 50)
    #     return

    
    @intent_handler('wigpi.intent')
    def ask_brain(self, message):
        """Send a query to the Wiggity brain.

        Saves the state to disk once in a while.
        """
        prompt = message.data.get("prompt")
        response = generate_response(prompt)
        self.speak(response)
        

    # def handle_fallback(self,message):
    #     utterance = message.data.get("utterance")
        
    #     if 'wiggity' in utterance:
    #         answer = self.ask_brain(utterance)
    #         self.speak(answer)
    #         return True
    #     else:
    #         return False

def create_skill():
    return Wigpi()