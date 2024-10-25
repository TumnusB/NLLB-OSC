# NLLB-OSC
 Super Simple OSC Bridge For [NLLB](https://github.com/gordicaleksa/Open-NLLB)

There are three launch arguments
--ip (**Default:127.0.0.1**) This is what IP the OSC Server and Client Should use
--serverport (**Default:5005**) This is what Port the OSC Server will recive data on
--clientport (**Default:5004**) This is what Port the OSC Client will send data on

The Server will take data in on /filter the arguments been

0. Input Text - E.G Hello World
1. Source Language - eng_Latn (English)
2. Target Language - deu_Latn (German)

See model used for all the diferent language tags

The OSC Client will respond on the OSC value of /translation with the tranlated text

There is a simpile python code to test as well as console display for testing

---

## Python Version
[3.12.7 using miniconda](https://docs.anaconda.com/miniconda/)

---
## Libaries Used
[transformers](https://github.com/huggingface/transformers)
[python-osc](https://github.com/attwad/python-osc)
[torch](https://pytorch.org/)

---

## Model Used
[Open-NLLB](https://github.com/gordicaleksa/Open-NLLB)
[Language_Tags](https://github.com/facebookresearch/flores/blob/main/flores200/README.md#languages-in-flores-200)
