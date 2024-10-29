from setuptools import setup

setup(
   name='jptranscription',
   version='0.1.1',
   description='Transcribes German words into Katakana using IPA',
   author='Philipp Schmitz',
   author_email='schmxtz@gmail.com',
   packages=['jptranscription', 'jptranscription.phonetics', 'jptranscription.transcription'],  #same as name
   install_requires=[], #external packages as dependencies
   include_package_data=True,
)