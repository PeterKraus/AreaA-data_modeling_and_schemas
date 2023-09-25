import numpy as np
import re
from datetime import datetime as dt
import pandas as pd
import json

from nomad.datamodel.metainfo.basesections import (
    ElementalComposition,
    Activity,
    PureSubstance,
    CompositeSystem,
    Measurement,
    Process,
    Collection,
    EntityReference,
    CompositeSystemReference,
    SectionReference,
    Experiment
)
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)
from nomad.parsing.tabular import TableData
from structlog.stdlib import (
    BoundLogger,
)
from nomad.metainfo import (
    MSection,
    Package,
    Quantity,
    SubSection,
    MEnum,
    Reference,
    Datetime,
    Section,
    QuantityReference
)
from nomad.datamodel.data import (
    EntryData,
    ArchiveSection,
    Author
)

m_package = Package(name='movpe_IKZ')


class Notes(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    notes = Quantity(
        type=str,
        a_eln={
            "component": "RichTextEditQuantity"
        },
    )


class Users(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    user = Quantity(
        type=Author,
        a_eln={
            "component": "AuthorEditQuantity"
        },
        shape=["*"],
    )


class ElementalComposition(ElementalComposition):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    element = Quantity(
        type=str,
        a_tabular={
            "name": "Substrate/Elements"
        },
        a_eln={
            "component": "StringEditQuantity"
        },
    )


class Parallelepiped(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    height = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "nanometer"
        },
        unit="nanometer",
    )
    width = Quantity(
        type=np.float64,
        description='substrate dimension X',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        a_tabular={
            "name": "Substrate/Size X"
        },
        unit="millimeter",
    )
    length = Quantity(
        type=np.float64,
        description='substrate dimension Y',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        a_tabular={
            "name": "Substrate/Size Y"
        },
        unit="millimeter",
    )
    surface_area = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter ** 2"
        },
        unit="millimeter ** 2",
    )
    volume = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter ** 3"
        },
        unit="millimeter ** 3",
    )


class Cylinder(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    height = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "nanometer"
        },
        unit="nanometer",
    )
    radius = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        unit="millimeter",
    )
    lower_cap_radius = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        unit="millimeter",
    )
    upper_cap_radius = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        unit="millimeter",
    )
    cap_surface_area = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter ** 2"
        },
        unit="millimeter ** 2",
    )
    lateral_surface_area = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter ** 2"
        },
        unit="millimeter ** 2",
    )
    volume = Quantity(
        type=np.float64,
        description='docs',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter ** 3"
        },
        unit="millimeter ** 3",
    )


class Geometry(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    parallelepiped = SubSection(
        section_def=Parallelepiped,
    )
    cylinder = SubSection(
        section_def=Cylinder,
    )


class Precursor(PureSubstance, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    name = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity",
            "label": "Substance Name"
        },
    )
    cas_number = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity",
            "label": "CAS number"
        },
    )


class Precursors(EntityReference):
    '''
    A section used for referencing a Precursor.
    '''
    reference = Quantity(
        type=Precursor,
        description='A reference to a NOMAD `Precursor` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Precursor Reference',
        ),
    )


class Substrate(CompositeSystem, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''

    m_def = Section(
        label_quantity='lab_id'
    )

    delivery_date = Quantity(
        type=Datetime,
        description='Date of the delivery',
        a_eln={
            "component": "DateTimeEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Delivery Date"
        },
    )
    lab_id = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Substrates"
        },
    )
    supplier = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Supplier"
        },
    )
    orientation = Quantity(
        type=str,
        description='crystallographic orientation of the substrate in [hkl]',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Orientation"
        },
    )
    miscut_b_angle = Quantity(
        type=str,
        description='crystallographic orientation of the substrate in [hkl]',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Miscut b angle"
        },
    )
    miscut_c_angle = Quantity(
        type=str,
        description='crystallographic orientation of the substrate in [hkl]',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Miscut c angle"
        },
    )
    miscut_c_orientation = Quantity(
        type=str,
        description='crystallographic orientation of the substrate in [hkl]',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Miscut c Orientation"
        },
    )
    doping_level = Quantity(
        type=np.float64,
        description='Chemical doping level of electrically conductive substrates',
        a_eln={
            "component": "NumberEditQuantity"},
        a_tabular={
            "name": "Substrate/Doping Level"},
    )
    doping_species = Quantity(
        type=str,
        description='Doping species to obtain electrical conductivity in the substrates',
        a_eln={
            "component": "StringEditQuantity"},
        a_tabular={
            "name": "Substrate/Doping species"},
    )
    as_received = Quantity(
        type=bool,
        description='Is the sample annealed?',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/As Received"
        },
    )
    etching = Quantity(
        type=bool,
        description='Usable Sample',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Etching"
        },
    )
    annealing = Quantity(
        type=bool,
        description='Usable Sample',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Annealing"
        },
    )
    annealing_temperature = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "Substrate/Annealing Temperature"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    re_etching = Quantity(
        type=bool,
        description='Usable Sample',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Re-Etching"
        },
    )
    re_annealing = Quantity(
        type=bool,
        description='Usable Sample',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Re-Annealing"
        },
    )
    epi_ready = Quantity(
        type=bool,
        description='Sample ready for epitaxy',
        a_eln={
            "component": "BoolEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Epi Ready"
        },
    )
    box = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Box"
        },
    )
    quality = Quantity(
        type=str,
        description='Defective Sample',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Quality"
        },
    )
    documentation = Quantity(
        type=str,
        description='pdf files containing certificate and other documentation',
        a_browser={
            "adaptor": "RawFileAdaptor"
        },
        a_eln={
            "component": "FileEditQuantity"
        },
    )
    notes = Quantity(
        type=str,
        description='Notes and comments.',
        a_eln={
            "component": "StringEditQuantity",
            "label": "Notes"
        },
    )
    geometry = SubSection(
        section_def=Geometry,
    )
    elemental_composition = SubSection(
        section_def=ElementalComposition,
        repeats=True,
    )


class Substrates(CompositeSystemReference):
    '''
    A section used for referencing a Substrate.
    '''

    reference = Quantity(
        type=Substrate,
        description='A reference to a NOMAD `Substrate` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Substrate Reference',
        ),
    )
    lab_id = Quantity(
        type=str,
        description='the Substrate used for the growth',
        a_tabular={
            "name": "GrowthRun/Substrate Name"
        },
        a_eln=ELNAnnotation(
            component='StringEditQuantity',
            label='Substrate ID',
        ),
    )

    def normalize(self, archive, logger: BoundLogger) -> None:
        '''
        The normalizer for the `Substrates` class.
        '''
        super(Substrates, self).normalize(archive, logger)

        if self.reference:
            setattr(self,'name', self.reference.lab_id)



class ParentSamples(EntityReference):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    reference = Quantity(
        type=CompositeSystem,
        description='A reference to a NOMAD `ParentSample` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Parent Sample Reference',
        ),
    )
    lab_id = Quantity(
        type=str,
        description='the sample used for this step of growth',
        a_tabular={
            "name": "GrowthRun/Previous Layer Name"
        },
        a_eln={
            "label": "Previous Layer ID"
        },
    )


class Sample(CompositeSystem, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section()
    name = Quantity(
        type=str,
        description='FILL',
        a_eln={
            "component": "StringEditQuantity"
        },
        a_tabular={
            "name": "Substrate/Material"
        },
    )
    lab_id = Quantity(
        type=str,
        description='the sample used for this step of growth',
        a_tabular={
            "name": "GrowthRun/Sample Name"
        },
        a_eln={
            "label": "Sample ID"
        },
    )
    test_quantities = Quantity(
        type=str,
        description='Test quantity',
        a_eln={
            "component": "StringEditQuantity"
        },
    )


class Samples(CompositeSystemReference):
    '''
    A section used for referencing a Sample.
    '''
    reference = Quantity(
        type=Sample,
        description='A reference to a NOMAD `Sample` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Sample Reference',
        ),
    )


class Bubblers(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        more={
            "label_quantity": "material"
        },)
    material = Quantity(
        type=str,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler Material"
        },
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    mass_flow_controller = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler MFC"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    pressure = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler Pressure"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mbar"
        },
        unit="mbar",
    )
    dilution = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler Dilution"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    source = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Source"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    inject = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Inject"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    temperature = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler Temp"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mbar"
        },
        unit="mbar",
    )
    partial_pressure = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Partial Pressure"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mbar"
        },
        unit="mbar",
    )
    molar_flux = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Bubbler Molar Flux"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mol / minute"
        },
        unit="mol / minute",
    )


class GasSource(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        more={
            "label_quantity": "material"
        },)
    material = Quantity(
        type=str,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Gas Material"
        },
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    mass_flow_controller = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Gas MFC"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    molar_flux = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Gas Molar Flux"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mbar"
        },
        unit="mbar",
    )


class GrowthRunStep(ArchiveSection):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    step_index = Quantity(
        type=str,
        description='the ID from RTG',
        a_tabular={
            "name": "GrowthRun/Step Index"
        },
        a_eln={
            "component": "StringEditQuantity",
        },
    )
    elapsed_time = Quantity(
        type=np.float64,
        description='Past time since process start',
        a_tabular={
            "name": "GrowthRun/Duration"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "minute"
        },
        unit="minute",
    )
    temperature_shaft = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/T Shaft"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    temperature_filament = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/T Filament"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    temperature_laytec = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/T LayTec"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    pressure = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Pressure"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "mbar"
        },
        unit="mbar",
    )
    rotation = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Rotation"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "rpm"
        },
        unit="rpm",
    )
    carrier_gas = Quantity(
        type=str,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Carrier Gas"
        },
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    push_gas_valve = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Pushgas Valve"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    uniform_valve = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Uniform Valve"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm ** 3 / minute"
        },
        unit="cm ** 3 / minute",
    )
    showerhead_distance = Quantity(
        type=np.float64,
        description='inner valve (0-200)',
        a_tabular={
            "name": "GrowthRun/Distance of Showerhead"
        },
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "millimeter"
        },
        unit="millimeter",
    )
    comments = Quantity(
        type=str,
        description='FILL THE DESCRIPTION',
        a_tabular={
            "name": "GrowthRun/Comments"
        },
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    bubblers = SubSection(
        section_def=Bubblers,
        repeats=True,
    )
    gas_source = SubSection(
        section_def=GasSource,
        repeats=True,
    )


class GrowthRun(Process, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln={
            "hide": [
                "steps"
            ]
        },
        # more={
        #     "label_quantity": "sample_id"
        # }
    )

    method = Quantity(
        type=str,
        default="Growth (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    lab_id = Quantity(
        type=str,
        description='the ID from RTG',
        a_tabular={
            "name": "GrowthRun/Recipe Name"
        },
        a_eln={
            "component": "StringEditQuantity",
            "label": "Growth ID"
        },
    )
    samples = SubSection(
        section_def=Samples,
    )
    parent_sample = SubSection(
        section_def=ParentSamples,
        repeats=True
    )
    substrate = SubSection(
        section_def=Substrates,
        repeats=True
    )
    growth_run_steps = SubSection(
        section_def=GrowthRunStep,
        repeats=True,
    )


class GrowthRuns(SectionReference):
    '''
    A section used for referencing a GrowthRun.
    '''
    reference = Quantity(
        type=GrowthRun,
        description='A reference to a NOMAD `GrowthRun` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Growth Run Reference',
        ),
    )


class InSituMonitorings(SectionReference):
    '''
    A section used for referencing a InSituMonitoring.
    '''
    reference = Quantity(
        type=Activity,
        description='A reference to a NOMAD `InSituMonitoring` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='In situ Monitoring Reference',
        ),
    )


class HallMeasurement(Measurement, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,
        more={
            "label_quantity": "sample_id"
        },)
    method = Quantity(
        type=str,
        default= "Hall (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    sample_id = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        a_eln={
            "component": "DateTimeEditQuantity"
        },
    )
    resistivity = Quantity(
        type=np.float64,
        description='FILL',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "ohm / cm"
        },
        unit="ohm / cm",
    )
    mobility = Quantity(
        type=np.float64,
        description='FILL',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "cm**2 / volt / second"
        },
        unit="cm**2 / volt / second",
    )
    carrier_concentration = Quantity(
        type=np.float64,
        description='FILL',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "1 / cm**3"
        },
        unit="1 / cm**3",
    )


class HallMeasurements(SectionReference):
    '''
    A section used for referencing a HallMeasurement.
    '''
    reference = Quantity(
        type=HallMeasurement,
        description='A reference to a NOMAD `HallMeasurement` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Hall Measurement Reference',
        ),
    )


class MovpeExperiment(TableData, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    growth_data_file = Quantity(
        type=str,
        description='Upload here the spreadsheet file containing the growth data',
        a_tabular_parser={
            "parsing_options": {
                "comment": "#"},
            "mapping_options": [
                {
                    "mapping_mode": "row",
                    "file_mode": "multiple_new_entries",
                    "sections": [
                        "growth_run/growth_run_steps"
                    ]
                },
                {
                    "mapping_mode": "row",
                    "file_mode": "current_entry",
                    "sections": [
                        "substrates"
                    ]
                }
            ]
        },
        a_browser={
            "adaptor": "RawFileAdaptor"},
        a_eln={
            "component": "FileEditQuantity"},
    )
    method = Quantity(
        type=str,
        default="Experiment (MOVPE IKZ)",
    )
    location = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    date = Quantity(
        type=Datetime,
        description='FILL',
        a_eln={
            "component": "DateTimeEditQuantity"
        },
    )
    notes = SubSection(
        section_def=Notes,
    )
    users = SubSection(
        section_def=Users,
    )
    precursors = SubSection(
        section_def=Precursors,
        repeats=True,
    )
    substrates = SubSection(
        section_def=Substrates,
        repeats=True,
    )
    parent_sample = SubSection(
        section_def=ParentSamples,
        repeats=True
    )
    grown_sample = SubSection(
        section_def=Samples,
        repeats=True
    )
    growth_run = SubSection(
        section_def=GrowthRuns,
        repeats=True,
    )
    in_situ_monitoring = SubSection(
        section_def=InSituMonitorings,
    )
    hall_measurement = SubSection(
        section_def=HallMeasurements,
    )


class SubstrateInventory(TableData, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    substrate_data_file = Quantity(
        type=str,
        description='Upload here the spreadsheet file containing the growth data',
        a_tabular_parser={
            "parsing_options": {
                "comment": "#"},
            "mapping_options": [
                {
                    "mapping_mode": "row",
                    "file_mode": "multiple_new_entries",
                    "sections": ["substrates"]}]},
        a_browser={
            "adaptor": "RawFileAdaptor"},
        a_eln={
            "component": "FileEditQuantity"},
    )
    substrates = SubSection(
        section_def=Substrates,
        repeats=True,
    )


class SubstratePreparationSteps(Activity):
    '''
    A section used for referencing Activity.
    '''
    m_def = Section()
    substrates = SubSection(
        section_def=Substrates,
        repeats=True,
    )


class Etching(SubstratePreparationSteps, Process, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    method = Quantity(
        type=str,
        default="Etching (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        description='FILL',
        a_eln={
            "component": "DateTimeEditQuantity",
            "label": "deposition_date"
        },
    )
    temperature = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    elapsed_time = Quantity(
        type=np.float64,
        description='Past time since process started (minutes)',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "minute"
        },
        unit="minute",
    )
    etching_reagents = SubSection(
        section_def=CompositeSystem,
        repeats=True
    )


class Annealing(SubstratePreparationSteps, Process, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    method = Quantity(
        type=str,
        default="Annealing (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        description='FILL',
        a_eln={
            "component": "DateTimeEditQuantity",
            "label": "deposition_date"
        },
    )
    temperature = Quantity(
        type=np.float64,
        description='FILL THE DESCRIPTION',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "celsius"
        },
        unit="celsius",
    )
    elapsed_time = Quantity(
        type=np.float64,
        description='Past time since process started (minutes)',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "minute"
        },
        unit="minute",
    )
    anealing_reagents = SubSection(
        section_def=CompositeSystemReference,
    )


class AFMmeasurement(SubstratePreparationSteps, Measurement, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,
        more={
            "label_quantity": "sample_id"
        },)
    method = Quantity(
        type=str,
        default="AFM (IKZ MOVPE)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity",
            "label": "Notes"
        },
    )
    image = Quantity(
        type=str,
        description='image showing the thickness measurement points',
        a_browser={
            "adaptor": "RawFileAdaptor"
        },
        a_eln={
            "component": "FileEditQuantity"
        },
    )
    sample_id = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        a_eln={
            "component": "DateTimeEditQuantity"
        },
    )
    roughness = Quantity(
        type=np.float64,
        description='RMS roughness value obtained by AFM',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "nanometer"
        },
        unit="nanometer",
    )
    surface_features = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )


class LightMicroscope(SubstratePreparationSteps, Measurement, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,
        more={
            "label_quantity": "sample_id"
        },)
    method = Quantity(
        type=str,
        default="Light Microscope (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity",
            "label": "Notes"
        },
    )
    image = Quantity(
        type=str,
        description='image',
        a_browser={
            "adaptor": "RawFileAdaptor"
        },
        a_eln={
            "component": "FileEditQuantity"
        },
    )
    sample_id = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        a_eln={
            "component": "DateTimeEditQuantity"
        },
    )


class Steps(SectionReference):
    '''
    A section used for referencing SubstratePreparationSteps.
    '''
    reference = Quantity(
        type=SubstratePreparationSteps,
        description='A reference to a NOMAD `SubstratePreparationSteps` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='SubstratePreparationSteps Reference',
        ),
    )


class SubstratePreparation(Process, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,)
    method = Quantity(
        type=str,
        default="Substrate Process (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    substrates = SubSection(
        section_def=Substrates,
        repeats=True,
    )
    steps = SubSection(
        section_def=Steps,
        repeats=True,
    )


class HRXRDmeasurement(Measurement, EntryData):
    '''
    Class autogenerated from yaml schema.
    '''
    m_def = Section(
        a_eln=None,
        more={
            "label_quantity": "sample_id"
        },)
    method = Quantity(
        type=str,
        default="HRXRD (MOVPE IKZ)",
    )
    description = Quantity(
        type=str,
        description='description',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    sample_id = Quantity(
        type=str,
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    datetime = Quantity(
        type=Datetime,
        a_eln={
            "component": "DateTimeEditQuantity"
        },
    )
    phase = Quantity(
        type=str,
        description='Phase type obtained from HRXRD',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    peak_position_2theta = Quantity(
        type=np.float64,
        description='Peak Position - 2theta',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "degree"
        },
        unit="degree",
    )
    peak_fwhm_2theta = Quantity(
        type=np.float64,
        description='Peak Position - 2theta',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "degree"
        },
        unit="degree",
    )
    peak_position_omega = Quantity(
        type=np.float64,
        description='Peak Position - Omega',
        a_eln={
            "component": "NumberEditQuantity",
            "defaultDisplayUnit": "degree"
        },
        unit="degree",
    )
    peak_fwhm_rocking_curve = Quantity(
        type=str,
        description='Peak FWHM Rocking Curve',
        a_eln={
            "component": "StringEditQuantity"
        },
    )
    reflection = Quantity(
        type=str,
        description='Peak FWHM Rocking Curve',
        a_eln={
            "component": "StringEditQuantity"
        },
    )


m_package.__init_metainfo__()
