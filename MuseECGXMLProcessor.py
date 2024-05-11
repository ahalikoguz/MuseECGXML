import xmltodict
import numpy as np
import base64
import array
import logging

class ECGXMLProcessor:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.leads_order = ["I", "II", "III", "aVR", "aVL", "aVF", "V1", "V2", "V3", "V4", "V5", "V6"]
        try:
            self.standard_ecg = self.process_xml()
        except Exception as e:
            logging.error(f"Failed to process XML file: {e}")
            raise ValueError("Invalid XML format or path")

    def process_xml(self):
        try:
            with open(self.xml_path, 'rb') as file:
                ecg_data = xmltodict.parse(file.read().decode('utf8'))
        except Exception as e:
            logging.error(f"Error reading or parsing XML file: {e}")
            raise

        try:
            Waveforms = ecg_data['RestingECG']['Waveform']
            leads = {}

            for lead in Waveforms[1]['LeadData']:  # Adjust index if necessary
                lead_data = lead['WaveFormData']
                lead_b64 = base64.b64decode(lead_data)
                lead_vals = np.array(array.array('h', lead_b64))
                leads[lead['LeadID']] = lead_vals

            # Calculate derived leads if not provided
            leads['III'] = np.subtract(leads['II'], leads['I'])
            leads['aVR'] = np.trunc(np.add(leads['I'], leads['II']) * (-0.5)).astype(int)
            leads['aVL'] = np.trunc(np.subtract(leads['I'], 0.5 * leads['II'])).astype(int)
            leads['aVF'] = np.trunc(np.subtract(leads['II'], 0.5 * leads['I'])).astype(int)

            # Reorder leads according to the standard lead order
            return np.column_stack([leads[lead] for lead in self.leads_order])
        except KeyError as e:
            logging.error(f"Key error in XML structure: {e}")
            raise ValueError("XML structure does not match expected format")

    def get_standard_ecg(self):
        return self.standard_ecg
