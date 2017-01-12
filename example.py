import uuid
from handler import SkyHandler

if __name__ == '__main__':
    sky = SkyHandler()
    sample_id = str(uuid.uuid4()).upper()
    sky.update_record('sample_table', sample_id, 'sample_field', 'sample_content')
