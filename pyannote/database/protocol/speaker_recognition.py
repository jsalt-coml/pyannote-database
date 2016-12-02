#!/usr/bin/env python
# encoding: utf-8

# The MIT License (MIT)

# Copyright (c) 2016 CNRS

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# AUTHORS
# Hervé BREDIN - http://herve.niderb.fr


from .protocol import Protocol


class SpeakerRecognitionProtocol(Protocol):
    """Speaker recognition protocol

    Parameters
    ----------
    preprocessors : dict or (key, preprocessor) iterable
        When provided, each protocol item (dictionary) are preprocessed, such
        that item[key] = preprocessor(**item). In case 'preprocessor' is not
        callable, it should be a string containing placeholder for item keys
        (e.g. {'wav': '/path/to/{uri}.wav'})
    """
    def trn_iter(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "trn_iter".')

    def dev_enroll_iter(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "dev_enroll_iter".')

    def dev_test_iter(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "dev_test_iter".')

    def dev_keys(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "dev_keys".')

    def tst_enroll_iter(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "tst_enroll_iter".')

    def tst_test_iter(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement "tst_test_iter".')

    def tst_keys(self):
        raise NotImplementedError(
            'Custom speaker recognition protocol '
            'should implement tst_keys".')

    def train(self):
        """Iterate over the training set

This will yield dictionaries with the followings keys:

* database: str
  unique database identifier
* uri: str
  unique recording identifier
* channel: int
  index of resource channel to use
* target: str
  unique target identifier

as well as keys coming from the provided preprocessors.

Usage
-----
>>> for item in protocol.train():
...     uri = item['uri']
...     channel = item['channel']
...     target = item['target']
        """
        for unique_name, item in self.trn_iter():
            yield unique_name, self.preprocess(item)

    def development_enroll(self):
        """Iterate over the development set enrollments

This will yield dictionaries with the followings keys:

* database: str
  unique database identifier
* uri: str
  uniform (or unique) resource identifier
* channel: int
  index of resource channel to use

as well as keys coming from the provided preprocessors.

Usage
-----
>>> for item in protocol.development_enroll():
...     uri = item['uri']
...     channel = item['channel']
        """
        for unique_name, item in self.dev_enroll_iter():
            yield unique_name, self.preprocess(item)

    def development_test(self):
        """Iterate over the development set tests

This will yield dictionaries with the followings keys:

* database: str
  unique database identifier
* uri: str
  uniform (or unique) resource identifier
* channel: int
  index of resource channel to use

as well as keys coming from the provided preprocessors.

Usage
-----
>>> for item in protocol.development_test():
...     uri = item['uri']
...     channel = item['channel']
        """
        for unique_name, item in self.dev_test_iter():
            yield unique_name, self.preprocess(item)

    def development_keys(self):
        return self.dev_keys()

    def test_enroll(self):
        """Iterate over the test set targets

This will yield dictionaries with the followings keys:

* database: str
  unique database identifier
* uri: str
  uniform (or unique) resource identifier
* channel: int
  index of resource channel to use
* target: str
  unique target identifier

as well as keys coming from the provided preprocessors.

Usage
-----
>>> for item in protocol.test_enroll():
...     uri = item['uri']
...     channel = item['channel']
...     target = item['target']
        """
        for unique_name, item in self.tst_enroll_iter():
            yield unique_name, self.preprocess(item)

    def test_test(self):
        """Iterate over the test set tests

This will yield dictionaries with the followings keys:

* database: str
  unique database identifier
* uri: str
  uniform (or unique) resource identifier
* channel: int
  index of resource channel to use

as well as keys coming from the provided preprocessors.

Usage
-----
>>> for item in protocol.test_test():
...     uri = item['uri']
...     channel = item['channel']
        """
        for unique_name, item in self.tst_test_iter():
            yield unique_name, self.preprocess(item)

    def test_keys(self):
        return self.tst_keys()
