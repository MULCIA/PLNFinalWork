Google Cloud Speech
===

# ![](https://cloud.google.com/_static/af7ae4b3fc/images/cloud/gcp-logo.svg)

##### [API](https://cloud.google.com/speech/) to convert audio to test

###### Created by Sergio Rodríguez ( [@serrodcal](https://github.com/serrodcal) )

---

# Introduction

- **API to convert audio to test.**
- Powerful neural network models in an easy to use API.
- Recognizes over 80 languages and variants.
- Accuracy improves over time.
- Return text result in real-time.
- Accurate in noisy environments.

---

# Sound

# ![200%](http://fisica.laguia2000.com/wp-content/uploads/2007/12/acustica041.gif)

---

# A/D converter

# ![150%](https://upload.wikimedia.org/wikipedia/commons/1/14/Conversor_AD.svg)

---

# Audio encoding

It has the following parameters:

- Channel.
- Sampling.
- Digital resolution.
- Bit rate.
- Lossy compression.

---

# Audio formats

- Note that audio format is not equivalent to audio encoding.
- Defines the format of the header of an audio file.
- Don't assume a kind of file has any particular encoding until you inspect its header.
- However, there is a 'formart' like `FLAC` which is both a file format and an encoding.

---

# Ways to use the API

- REST.
- Client libraries.
- RPC.

---

# API Rest

- All URIs below are relative to https://speech.googleapis.com
- This service provides the following discovery document: https://speech.googleapis.com/$discovery/rest?version=v1

---

# Speech Recognition

- Performs asynchronous speech recognition.
- `POST /v1/speech:longrunningrecognize`
```
{
  "config": { #information to the recognizer
    object(RecognitionConfig)
  },
  "audio": { # audio data
    object(RecognitionAudio)
  },
}
```

---

# Speech Recognition

- Performs synchronous speech recognition.
- `POST /v1/speech:recognize`
```
{
  "config": { #information to the recognizer
    object(RecognitionConfig)
  },
  "audio": { # audio data
    object(RecognitionAudio)
  },
}
```

---

# Speech Recognition

- In longrunningrecognize the response contains an instance of `Operation`.
- In recognize the response is:
```
{
  "results": [ # Array for alternatives
    {
      object(SpeechRecognitionResult)
    }
  ],
}
```

---

# Speech Recognition

- In asynchronous, we can get the latest status of a long-running operation.
- `GET /v1/operations/{name}`

---

# Speech Recognition

- Response for operation resource:

```
{
  "name": string,
  "metadata": {
    "@type": string,
    field1: ...,
    ...
  },
  "done": boolean,
  "error": { # error case, done equals to false
    object(Status)
  },
  "response": { # success case, done equals to true
    "@type": string,
    field1: ...,
    ...
  }, # Could be several responses
}
```
---

# Client libraries

- There are several client libraries: C#, GO, Java, Node.js, PHP, Python and Ruby.
- In python we must use PIP to install the client library:
```
pip install --upgrade google-cloud-speech
```
- In Java we must use Maven o Gradle to provide the dependency for our project:

```
<dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-speech</artifactId>
    <version>0.17.1-alpha</version>
</dependency>
```

---

# Client libraries

- At now, just import it.

```
# Imports the Google Cloud client library
from google.cloud import speech

# Instantiates a client
speech_client = speech.Client()

# Rest of code
```

--- 

# Behind Google Cloud Speech

- 

