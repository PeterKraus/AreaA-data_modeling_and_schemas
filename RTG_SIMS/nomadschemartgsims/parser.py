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
from nomadschemartgsims.schema import RTGSIMSMeasurement #HZBUnoldLabThermalEvaporation

class RTGSIMSDPFile(EntryData):
    measurement = Quantity(
        type=RTGSIMSMeasurement,
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
        )
    )


class SIMSParser(MatchingParser):

    def __init__(self):
        super().__init__(
            name='NOMAD RTG SIMS schema and parser plugin',
            code_name= 'RTG SIMS Parser',#'HZB Unold Lab Parser',
            code_homepage='https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas',
            supported_compressions=['gz', 'bz2', 'xz']
        )

    def parse(self, mainfile: str, archive: EntryArchive, logger) -> None:
        data_file = mainfile.split('/')[-1]
        data_file_with_path = mainfile.split("raw/")[-1]
        entry = RTGSIMSMeasurement.m_from_dict(RTGSIMSMeasurement.m_def.a_template)
        entry.data_file = data_file_with_path
        file_name = f'{data_file[:-9]}.archive.json'
        #entry.normalize(archive, logger)
        archive.data = RTGSIMSDPFile(measurement=create_archive(entry,archive,file_name))
        archive.metadata.entry_name = data_file + ' measurement file'