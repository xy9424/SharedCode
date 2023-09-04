import unittest
import logging
from EntityAnalyzer import extract_entities

class TestEntityAnalyzer(unittest.TestCase):
    # 创建一个日志记录器
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # 创建一个文件处理器
    file_handler = logging.FileHandler('my_log_file.log')
    file_handler.setLevel(logging.DEBUG)

    # 创建一个控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # 创建一个格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 将格式化器添加到处理器
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    def test_extract_entities_empty(self):
        # Test empty source code
        source_code = ''
        entities = extract_entities(source_code)
        self.assertEqual(entities, set())

    def test_extract_entities_single(self):
        # Test source code with a single entity
        source_code = 'This code uses TensorFlow.'
        entities = extract_entities(source_code)
        self.assertEqual(entities, {'tensorflow'})

    def test_extract_entities_multiple(self):
        # Test source code with multiple entities
        source_code = 'This code uses PyTorch and NumPy.'
        entities = extract_entities(source_code)
        self.assertEqual(entities, {'pytorch', 'numpy'})

    def test_extract_entities_none(self):
        # Test source code with no entities
        source_code = 'This code does not use any libraries.'
        entities = extract_entities(source_code)
        self.assertEqual(entities, set())

    def test_extract_entities_case(self):
        # Test source code with entities in different cases
        source_code = 'This code uses TensorFlow and PyTorch.'
        entities = extract_entities(source_code)
        self.assertEqual(entities, {'tensorflow', 'pytorch'})

    def test_extract_entities_duplicates(self):
        # Test source code with duplicate entities
        source_code = 'This code uses TensorFlow and TensorFlow.'
        entities = extract_entities(source_code)
        self.logger.debug(entities)
        self.assertEqual(entities, {'tensorflow'})

    def test_extract_entities_javasimple(self):
        # Test source code with duplicate entities
        source_code = 'This code uses Database， JDBC . import java.io.*; import java.db.*; import java.util.*;'
        entities = extract_entities(source_code)
        self.logger.debug(entities)
        self.assertEqual(entities, {'Java'})


if __name__ == '__main__':
    unittest.main()