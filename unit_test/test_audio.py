import unittest
from unittest.mock import patch, mock_open
from audio import transcribes_audio

class TestAudioTranscription(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=b"fake audio data")
    @patch('openai.OpenAI.audio.transcriptions.create')
    def test_transcribes_audio(self, mock_create, mock_file):
        # Mock the OpenAI API response
        mock_create.return_value = {
            "text": "This is a test transcription."
        }
        
        audiopath = "fakepath/audiofile.mp3"
        
        # Call the transcribes_audio function
        result = transcribes_audio(audiopath)
        
        # Ensure the file was opened correctly
        mock_file.assert_called_once_with(audiopath, 'rb')
        
        # Ensure the OpenAI API was called with the correct parameters
        mock_create.assert_called_once_with(model='whisper-1', file=mock_file())
        
        # Check if the result matches the mocked API response
        self.assertEqual(result, {"text": "This is a test transcription."})

if __name__ == '__main__':
    unittest.main()
