import sys
from unittest.mock import patch, MagicMock

from pytest import fixture

from utils.logging_service import LoggingService, default_logging_format, default_level


@fixture(name='logging_service')
def _logging_service():
    expected_name = 'test'

    logging_service = LoggingService(expected_name)

    assert expected_name == logging_service.name
    assert default_logging_format == logging_service.logging_format
    assert default_level == logging_service.level
    assert logging_service._logger is None

    return logging_service


@patch('utils.logging_service.LoggingService._build_stream_handler')
@patch('utils.logging_service.logging')
def test_get_logger(mock_logging, mock_build_stream_handler, logging_service):
    logger = logging_service.logger

    mock_logging.getLogger.assert_called_with(logging_service.name)
    mock_logging.getLogger.return_value.setLevel.assert_called_with(logging_service.level)
    mock_logging.getLogger.return_value.addHandler.assert_called_with(mock_build_stream_handler.return_value)

    assert mock_logging.getLogger.return_value == logger

    _logger = logging_service.logger

    assert logger is _logger
    assert 1 == mock_logging.getLogger.call_count


@patch('utils.logging_service.logging')
def test_create_stream_handler(mock_logging, logging_service):
    mock_formatter = MagicMock()
    mock_logging.Formatter.return_value = mock_formatter

    stream_handler = logging_service._build_stream_handler(sys.stdout)

    mock_logging.Formatter.assert_called_with(logging_service.logging_format)
    mock_logging.StreamHandler.assert_called_with(sys.stdout)
    mock_logging.StreamHandler.return_value.setLevel.assert_called_with(logging_service.level)
    mock_logging.StreamHandler.return_value.setFormatter.assert_called_with(mock_formatter)

    assert mock_logging.StreamHandler.return_value == stream_handler


def test_info(logging_service):
    mock_logger = MagicMock()
    logging_service._logger = mock_logger

    logging_service.info('message')

    mock_logger.info.assert_called_with('message')


def test_warning(logging_service):
    mock_logger = MagicMock()
    logging_service._logger = mock_logger

    logging_service.warning('message')

    mock_logger.warning.assert_called_with('message')


def test_exception(logging_service):
    mock_logger = MagicMock()
    logging_service._logger = mock_logger

    logging_service.exception('message')

    mock_logger.exception.assert_called_with('message')
