"""
Tests for document converters.
"""

import unittest
from pathlib import Path
import tempfile
import os
from unittest.mock import patch, MagicMock
from converters.pdf_converter import PDFConverter
from converters.docx_converter import DOCXConverter
from converters.image_converter import ImageConverter
from converters.base_converter import BaseConverter


class TestBaseConverter(unittest.TestCase):
    """Tests for base converter class."""
    
    def setUp(self):
        # Use a concrete implementation for testing
        self.converter = ImageConverter()
    
    def test_converter_exists(self):
        """Test if converter exists."""
        self.assertIsNotNone(self.converter)
    
    def test_create_markdown_header_level_1(self):
        """Test creating Markdown header level 1."""
        header = self.converter._create_markdown_header('Test', level=1)
        self.assertEqual(header, '# Test\n\n')
    
    def test_create_markdown_header_level_2(self):
        """Test creating Markdown header level 2."""
        header = self.converter._create_markdown_header('Test', level=2)
        self.assertEqual(header, '## Test\n\n')
    
    def test_create_markdown_header_level_6(self):
        """Test creating Markdown header level 6."""
        header = self.converter._create_markdown_header('Test', level=6)
        self.assertEqual(header, '###### Test\n\n')
    
    def test_escape_markdown(self):
        """Test escaping special Markdown characters."""
        text = "Hello *world* with [link] and _underscore_"
        escaped = self.converter._escape_markdown(text)
        
        # Check if characters were properly escaped
        self.assertIn('\\*', escaped)
        self.assertIn('\\[', escaped)
        self.assertIn('\\_', escaped)


class TestPDFConverter(unittest.TestCase):
    """Tests for PDF converter."""
    
    def setUp(self):
        self.converter = PDFConverter()
        self.temp_dir = tempfile.mkdtemp()
    
    def test_converter_exists(self):
        """Test if PDF converter exists."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test if PDFConverter inherits from BaseConverter."""
        self.assertIsInstance(self.converter, BaseConverter)
    
    def test_table_to_markdown_basic(self):
        """Test converting simple table to Markdown."""
        table = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row 1 Col 1', 'Row 1 Col 2', 'Row 1 Col 3'],
            ['Row 2 Col 1', 'Row 2 Col 2', 'Row 2 Col 3'],
        ]
        
        result = self.converter._table_to_markdown(table)
        
        # Verify
        self.assertIn('Header 1', result)
        self.assertIn('---', result)
        self.assertIn('|', result)
        self.assertIn('Row 1 Col 1', result)
    
    def test_table_to_markdown_with_none_values(self):
        """Test converting table with None values."""
        table = [
            ['Col 1', 'Col 2'],
            ['Value 1', None],
            [None, 'Value 2'],
        ]
        
        result = self.converter._table_to_markdown(table)
        
        # Verify - no exceptions should be thrown
        self.assertIsNotNone(result)
        self.assertIn('|', result)
    
    def test_table_to_markdown_empty_table(self):
        """Test converting empty table."""
        table = []
        result = self.converter._table_to_markdown(table)
        self.assertEqual(result, "")
    
    def test_table_to_markdown_single_row(self):
        """Test converting table with one row."""
        table = [['Only', 'One', 'Row']]
        result = self.converter._table_to_markdown(table)
        
        self.assertIn('Only', result)
        self.assertIn('---', result)
    
    def test_convert_nonexistent_file(self):
        """Test converting non-existent PDF file."""
        result = self.converter.convert('/nonexistent/file.pdf')
        self.assertIsNone(result)
    
    def tearDown(self):
        """Clean up after tests."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


class TestDOCXConverter(unittest.TestCase):
    """Tests for DOCX converter."""
    
    def setUp(self):
        self.converter = DOCXConverter()
    
    def test_converter_exists(self):
        """Test if DOCX converter exists."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test if DOCXConverter inherits from BaseConverter."""
        self.assertIsInstance(self.converter, BaseConverter)
    
    def test_get_header_level_heading_1(self):
        """Test header level for Heading 1."""
        self.assertEqual(self.converter._get_header_level('Heading 1'), 1)
    
    def test_get_header_level_heading_2(self):
        """Test header level for Heading 2."""
        self.assertEqual(self.converter._get_header_level('Heading 2'), 2)
    
    def test_get_header_level_heading_3(self):
        """Test header level for Heading 3."""
        self.assertEqual(self.converter._get_header_level('Heading 3'), 3)
    
    def test_get_header_level_heading_6(self):
        """Test header level for Heading 6."""
        self.assertEqual(self.converter._get_header_level('Heading 6'), 6)
    
    def test_get_header_level_normal(self):
        """Test header level for Normal (not a header)."""
        self.assertEqual(self.converter._get_header_level('Normal'), 0)
    
    def test_get_header_level_case_insensitive(self):
        """Test if check is case-insensitive."""
        self.assertEqual(self.converter._get_header_level('heading 1'), 1)
        self.assertEqual(self.converter._get_header_level('HEADING 2'), 2)
    
    def test_format_run_bold(self):
        """Test formatting bold text."""
        mock_run = MagicMock()
        mock_run.text = 'Bold Text'
        mock_run.bold = True
        mock_run.italic = False
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        self.assertEqual(result, '**Bold Text**')
    
    def test_format_run_italic(self):
        """Test formatting italic text."""
        mock_run = MagicMock()
        mock_run.text = 'Italic Text'
        mock_run.bold = False
        mock_run.italic = True
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        self.assertEqual(result, '*Italic Text*')
    
    def test_format_run_bold_and_italic(self):
        """Test formatting bold and italic text."""
        mock_run = MagicMock()
        mock_run.text = 'Bold Italic'
        mock_run.bold = True
        mock_run.italic = True
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        # Should contain both formatting types
        self.assertIn('**', result)
        self.assertIn('*', result)
    
    def test_table_to_markdown(self):
        """Test converting DOCX table to Markdown."""
        # Create mock table
        mock_table = MagicMock()
        mock_row1 = MagicMock()
        mock_row2 = MagicMock()
        
        mock_cell1 = MagicMock()
        mock_cell2 = MagicMock()
        mock_cell3 = MagicMock()
        mock_cell4 = MagicMock()
        
        mock_paragraph1 = MagicMock()
        mock_paragraph2 = MagicMock()
        mock_paragraph3 = MagicMock()
        mock_paragraph4 = MagicMock()
        
        mock_paragraph1.text = 'Header 1'
        mock_paragraph2.text = 'Header 2'
        mock_paragraph3.text = 'Data 1'
        mock_paragraph4.text = 'Data 2'
        
        mock_cell1.paragraphs = [mock_paragraph1]
        mock_cell2.paragraphs = [mock_paragraph2]
        mock_cell3.paragraphs = [mock_paragraph3]
        mock_cell4.paragraphs = [mock_paragraph4]
        
        mock_row1.cells = [mock_cell1, mock_cell2]
        mock_row2.cells = [mock_cell3, mock_cell4]
        
        mock_table.rows = [mock_row1, mock_row2]
        
        result = self.converter._table_to_markdown(mock_table)
        
        self.assertIn('|', result)
        self.assertIn('---', result)
    
    def test_convert_nonexistent_file(self):
        """Test converting non-existent DOCX file."""
        result = self.converter.convert('/nonexistent/file.docx')
        self.assertIsNone(result)


class TestImageConverter(unittest.TestCase):
    """Tests for image converter."""
    
    def setUp(self):
        self.converter = ImageConverter()
        self.temp_dir = tempfile.mkdtemp()
    
    def test_converter_exists(self):
        """Test if image converter exists."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test if ImageConverter inherits from BaseConverter."""
        self.assertIsInstance(self.converter, BaseConverter)
    
    def test_get_mime_type_png(self):
        """Test MIME type dla PNG."""
        self.assertEqual(self.converter._get_mime_type('.png'), 'image/png')
    
    def test_get_mime_type_jpg(self):
        """Test MIME type dla JPG."""
        self.assertEqual(self.converter._get_mime_type('.jpg'), 'image/jpeg')
    
    def test_get_mime_type_jpeg(self):
        """Test MIME type dla JPEG."""
        self.assertEqual(self.converter._get_mime_type('.jpeg'), 'image/jpeg')
    
    def test_get_mime_type_gif(self):
        """Test MIME type dla GIF."""
        self.assertEqual(self.converter._get_mime_type('.gif'), 'image/gif')
    
    def test_get_mime_type_bmp(self):
        """Test MIME type dla BMP."""
        self.assertEqual(self.converter._get_mime_type('.bmp'), 'image/bmp')
    
    def test_get_mime_type_webp(self):
        """Test MIME type dla WebP."""
        self.assertEqual(self.converter._get_mime_type('.webp'), 'image/webp')
    
    def test_get_mime_type_unknown(self):
        """Test MIME type dla nieznanego formatu."""
        self.assertEqual(self.converter._get_mime_type('.unknown'), 'image/png')
    
    def test_convert_nonexistent_image(self):
        """Test konwersji nieistniejącego obrazu."""
        result = self.converter.convert('/nonexistent/image.png')
        self.assertIsNone(result)
    
    def tearDown(self):
        """Clean up after tests."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


class TestUtilsFunctions(unittest.TestCase):
    """Testy dla funkcji utility."""
    
    def test_utils_import(self):
        """Test czy utils można importować."""
        try:
            from utils import is_supported, get_supported_extensions
            self.assertIsNotNone(is_supported)
            self.assertIsNotNone(get_supported_extensions)
        except ImportError:
            self.fail("Nie można zaimportować utils")
    
    def test_is_supported_pdf(self):
        """Test czy PDF jest obsługiwany."""
        from utils import is_supported
        self.assertTrue(is_supported('document.pdf'))
    
    def test_is_supported_docx(self):
        """Test czy DOCX jest obsługiwany."""
        from utils import is_supported
        self.assertTrue(is_supported('document.docx'))
    
    def test_is_supported_image(self):
        """Test czy obrazy są obsługiwane."""
        from utils import is_supported
        self.assertTrue(is_supported('image.png'))
        self.assertTrue(is_supported('image.jpg'))
    
    def test_is_not_supported_txt(self):
        """Test czy TXT nie jest obsługiwany."""
        from utils import is_supported
        self.assertFalse(is_supported('document.txt'))


if __name__ == '__main__':
    unittest.main()
