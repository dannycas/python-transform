"""
Testy dla konwerterów dokumentów.
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
    """Testy dla klasy bazowej konwertera."""
    
    def setUp(self):
        # Używamy konkretnej implementacji do testowania
        self.converter = ImageConverter()
    
    def test_converter_exists(self):
        """Test czy konwerter istnieje."""
        self.assertIsNotNone(self.converter)
    
    def test_create_markdown_header_level_1(self):
        """Test tworzenia nagłówka Markdown poziom 1."""
        header = self.converter._create_markdown_header('Test', level=1)
        self.assertEqual(header, '# Test\n\n')
    
    def test_create_markdown_header_level_2(self):
        """Test tworzenia nagłówka Markdown poziom 2."""
        header = self.converter._create_markdown_header('Test', level=2)
        self.assertEqual(header, '## Test\n\n')
    
    def test_create_markdown_header_level_6(self):
        """Test tworzenia nagłówka Markdown poziom 6."""
        header = self.converter._create_markdown_header('Test', level=6)
        self.assertEqual(header, '###### Test\n\n')
    
    def test_escape_markdown(self):
        """Test escapeowania znaków specjalnych Markdown."""
        text = "Hello *world* with [link] and _underscore_"
        escaped = self.converter._escape_markdown(text)
        
        # Sprawdzenie czy znaki zostały zachowane (escaped)
        self.assertIn('\\*', escaped)
        self.assertIn('\\[', escaped)
        self.assertIn('\\_', escaped)


class TestPDFConverter(unittest.TestCase):
    """Testy dla konwertera PDF."""
    
    def setUp(self):
        self.converter = PDFConverter()
        self.temp_dir = tempfile.mkdtemp()
    
    def test_converter_exists(self):
        """Test czy konwerter PDF istnieje."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test czy PDFConverter dziedziczy z BaseConverter."""
        self.assertIsInstance(self.converter, BaseConverter)
    
    def test_table_to_markdown_basic(self):
        """Test konwersji prostej tabeli na Markdown."""
        table = [
            ['Header 1', 'Header 2', 'Header 3'],
            ['Row 1 Col 1', 'Row 1 Col 2', 'Row 1 Col 3'],
            ['Row 2 Col 1', 'Row 2 Col 2', 'Row 2 Col 3'],
        ]
        
        result = self.converter._table_to_markdown(table)
        
        # Sprawdzenia
        self.assertIn('Header 1', result)
        self.assertIn('---', result)
        self.assertIn('|', result)
        self.assertIn('Row 1 Col 1', result)
    
    def test_table_to_markdown_with_none_values(self):
        """Test konwersji tabeli z wartościami None."""
        table = [
            ['Col 1', 'Col 2'],
            ['Value 1', None],
            [None, 'Value 2'],
        ]
        
        result = self.converter._table_to_markdown(table)
        
        # Sprawdzenia - żadne wyjątki nie powinny być rzucane
        self.assertIsNotNone(result)
        self.assertIn('|', result)
    
    def test_table_to_markdown_empty_table(self):
        """Test konwersji pustej tabeli."""
        table = []
        result = self.converter._table_to_markdown(table)
        self.assertEqual(result, "")
    
    def test_table_to_markdown_single_row(self):
        """Test konwersji tabeli z jednym wierszem."""
        table = [['Only', 'One', 'Row']]
        result = self.converter._table_to_markdown(table)
        
        self.assertIn('Only', result)
        self.assertIn('---', result)
    
    def test_convert_nonexistent_file(self):
        """Test konwersji nieistniejącego pliku PDF."""
        result = self.converter.convert('/nonexistent/file.pdf')
        self.assertIsNone(result)
    
    def tearDown(self):
        """Czyszczenie po testach."""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)


class TestDOCXConverter(unittest.TestCase):
    """Testy dla konwertera DOCX."""
    
    def setUp(self):
        self.converter = DOCXConverter()
    
    def test_converter_exists(self):
        """Test czy konwerter DOCX istnieje."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test czy DOCXConverter dziedziczy z BaseConverter."""
        self.assertIsInstance(self.converter, BaseConverter)
    
    def test_get_header_level_heading_1(self):
        """Test poziomu nagłówka Heading 1."""
        self.assertEqual(self.converter._get_header_level('Heading 1'), 1)
    
    def test_get_header_level_heading_2(self):
        """Test poziomu nagłówka Heading 2."""
        self.assertEqual(self.converter._get_header_level('Heading 2'), 2)
    
    def test_get_header_level_heading_3(self):
        """Test poziomu nagłówka Heading 3."""
        self.assertEqual(self.converter._get_header_level('Heading 3'), 3)
    
    def test_get_header_level_heading_6(self):
        """Test poziomu nagłówka Heading 6."""
        self.assertEqual(self.converter._get_header_level('Heading 6'), 6)
    
    def test_get_header_level_normal(self):
        """Test poziomu nagłówka Normal (nie jest nagłówkiem)."""
        self.assertEqual(self.converter._get_header_level('Normal'), 0)
    
    def test_get_header_level_case_insensitive(self):
        """Test czy sprawdzanie jest case-insensitive."""
        self.assertEqual(self.converter._get_header_level('heading 1'), 1)
        self.assertEqual(self.converter._get_header_level('HEADING 2'), 2)
    
    def test_format_run_bold(self):
        """Test formatowania tekstu pogrubionego."""
        mock_run = MagicMock()
        mock_run.text = 'Bold Text'
        mock_run.bold = True
        mock_run.italic = False
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        self.assertEqual(result, '**Bold Text**')
    
    def test_format_run_italic(self):
        """Test formatowania tekstu kursywnego."""
        mock_run = MagicMock()
        mock_run.text = 'Italic Text'
        mock_run.bold = False
        mock_run.italic = True
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        self.assertEqual(result, '*Italic Text*')
    
    def test_format_run_bold_and_italic(self):
        """Test formatowania tekstu pogrubionego i kursywnego."""
        mock_run = MagicMock()
        mock_run.text = 'Bold Italic'
        mock_run.bold = True
        mock_run.italic = True
        mock_run.underline = False
        
        result = self.converter._format_run(mock_run)
        # Powinno zawierać oba formatowania
        self.assertIn('**', result)
        self.assertIn('*', result)
    
    def test_table_to_markdown(self):
        """Test konwersji tabeli DOCX na Markdown."""
        # Tworzymy mock tabeli
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
        """Test konwersji nieistniejącego pliku DOCX."""
        result = self.converter.convert('/nonexistent/file.docx')
        self.assertIsNone(result)


class TestImageConverter(unittest.TestCase):
    """Testy dla konwertera obrazów."""
    
    def setUp(self):
        self.converter = ImageConverter()
        self.temp_dir = tempfile.mkdtemp()
    
    def test_converter_exists(self):
        """Test czy konwerter obrazów istnieje."""
        self.assertIsNotNone(self.converter)
    
    def test_converter_is_base_converter(self):
        """Test czy ImageConverter dziedziczy z BaseConverter."""
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
        """Czyszczenie po testach."""
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
