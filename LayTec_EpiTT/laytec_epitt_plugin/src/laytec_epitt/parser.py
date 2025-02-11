#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from nomad.datamodel import EntryArchive
from nomad.metainfo import (
    MSection,
    Quantity,
    Section
)
from nomad.parsing import MatchingParser
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)
from nomad.datamodel.data import (
    EntryData,
)

#from nomad_material_processing.utils import create_archive
from nomad_measurements.utils import create_archive
from laytec_epitt.schema import (
    LayTec_EpiTT_Measurement,
    IKZLayTecEpiTTCategory
)

class LayTecEpiTTFile(EntryData):
    """
    Contains the raw file from LayTecEpiTT in situ monitoring
    """
    m_def = Section(
        categories=[IKZLayTecEpiTTCategory]
    )
    measurement = Quantity(
        type=LayTec_EpiTT_Measurement,
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
        )
    )


class EpiTTParser(MatchingParser):

    def __init__(self):
        super().__init__(
            name='NOMAD LayTec EpiTT schema and parser plugin',
            code_name= 'EpiTT Parser',#'HZB Unold Lab Parser',
            code_homepage='https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas',
            supported_compressions=['gz', 'bz2', 'xz']
        )

    def parse(self, mainfile: str, archive: EntryArchive, logger) -> None:
        data_file = mainfile.split('/')[-1]
        data_file_with_path = mainfile.split("raw/")[-1]
        entry = LayTec_EpiTT_Measurement.m_from_dict(LayTec_EpiTT_Measurement.m_def.a_template)#()#.m_from_dict(LayTec_EpiTT_Measurement.m_def.a_template)
        entry.data_file = data_file_with_path
        file_name = f'{data_file[:-4]}.archive.json'
        #entry.normalize(archive, logger)
        archive.data = LayTecEpiTTFile(measurement=create_archive(entry,archive,file_name))
        archive.metadata.entry_name = data_file + ' in situ measurement file'