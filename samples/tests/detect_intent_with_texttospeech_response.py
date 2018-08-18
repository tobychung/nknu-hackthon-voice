# Copyright 2018, Google LLC
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

from __future__ import absolute_import
import os

from ..detect_intent_with_texttospeech_response import \
    detect_intent_with_texttospeech_response

PROJECT_ID = os.getenv('GCLOUD_PROJECT')
SESSION_ID = 'fake_session_for_testing'
TEXTS = ["hello"]


def test_detect_intent_with_sentiment_analysis(capsys):
    detect_intent_with_texttospeech_response(PROJECT_ID, SESSION_ID, TEXTS,
                                             'en-US')
    out, _ = capsys.readouterr()

    assert 'Audio content written to file' in out
    statinfo = os.stat('output.wav')
    assert statinfo.st_size > 0
    os.remove('output.wav')
    assert not os.path.isfile('output.wav')
