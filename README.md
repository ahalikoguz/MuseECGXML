# MuseECGXML

## Overview
`MuseECGXML` is a Python utility designed to extract 12-lead ECG data from MUSE XML files and convert them into NumPy arrays. This tool is especially useful for researchers, clinicians, and developers engaged in ECG data analysis, research, or application development.

## Features
- **Read MUSE XML**: Efficiently parses MUSE-formatted XML files containing ECG data.
- **Extract 12 Leads**: Extracts all standard 12 leads from the ECG data.
- **Output to NumPy**: Converts ECG leads into NumPy arrays for easy use in scientific computing.

## Acknowledgements

Special thanks to everyone who contributed to testing and refining this utility, as well as to other repositories that inspired this project:

    [will2hew/ECGXMLReader](https://github.com/will2hew/ECGXMLReader)

## Installation and Setup

Ensure `MuseECGXMLProcessor.py` is in your project directory or a directory in your PYTHONPATH. Here's how to use it:

```python
import logging
from MuseECGXMLProcessor import ECGXMLProcessor

# Setup logging
logging.basicConfig(level=logging.INFO)

# Specify the path to your MUSE XML file
xml_file_path = 'path_to_your_MUSE_file.xml'

# Initialize the processor and load data
try:
    ecg_processor = ECGXMLProcessor(xml_file_path)
    ecg_data = ecg_processor.get_standard_ecg()
    print("ECG Data Shape:", ecg_data.shape)
except Exception as e:
    logging.error(f"An error occurred: {e}")
