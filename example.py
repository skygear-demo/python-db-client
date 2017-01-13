import uuid
from handler import SkyHandler

if __name__ == '__main__':
    sky = SkyHandler()
    sample_id = str(uuid.uuid4()).upper()
    sky.update_record('sample_table', sample_id, {
            'sample_field_1': 'sample_content_1',
            'sample_field_2': 'sample_content_2',
            'sample_field_3': 'sample_content_3'
        }
    )
