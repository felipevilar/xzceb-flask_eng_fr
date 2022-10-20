"""
  Translation funcions to
  English-French and Franch-English
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url= os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-12-09',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
      Translate english text to french
    """
    try:
      translation = language_translator.translate(
          text=english_text,
          model_id='en-fr'
      ).get_result()
      french_text = translation['translations'][0]['translation']
      return french_text
    except ValueError:
      print("Invalid value input!")
    except:
      print("Something else went wrong!")

def french_to_english(french_text):
    """
      Translate french text to english
    """
    try:
      translation = language_translator.translate(
          text=french_text,
          model_id='fr-en'
      ).get_result()
      english_text = translation['translations'][0]['translation']
      return english_text
    except ValueError:
      print("Invalid value input!")
    except:
      print("Something else went wrong!")
