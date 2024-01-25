import unittest
from unittest.mock import patch, MagicMock
from paper_summary import SummarizePaperPlugin

class TestSummarizePaperPlugin(unittest.TestCase):
    @patch('paper_summary.PyPDFLoader')
    @patch('paper_summary.AzureChatOpenAI')
    def test_call(self, mock_azure_chat, mock_pdf_loader):
        # Arrange
        mock_azure_chat.return_value.invoke.return_value.content = 'Mocked summary'
        mock_pdf_loader.return_value.load.return_value = [MagicMock(page_content='Mocked page content') for _ in range(5)]
        plugin = SummarizePaperPlugin()
        plugin.config = {
            "api_type": "openai",
            "api_base": "mocked_base",
            "api_key": "mocked_key",
            "api_version": "mocked_version",
            "deployment_name": "mocked_deployment"
        }

        # Act
        summary, description = plugin('mocked_path')

        # Assert
        self.assertEqual(summary, 'Mocked summary')
        self.assertIn('We have summarized 5 pages of this paper.', description)

if __name__ == '__main__':
    unittest.main()