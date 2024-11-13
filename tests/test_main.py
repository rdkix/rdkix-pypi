import pytest

def test_descriptor():
    from rdkix.Chem import Descriptors
    # Was 209 but changed to 211 in Release_2023_09_1
    # Is 210 from Release_2023_09_3
    assert len(Descriptors._descList) == 210


def test_3d_descriptors():
    # from https://github.com/rdkix/rdkix/blob/master/rdkix/Chem/UnitTestDescriptors.py
    from rdkix import Chem
    from rdkix.Chem import AllChem, Descriptors3D

    mol = Chem.MolFromSmiles('CCCO')
    
    # test function returns expected outputs
    AllChem.EmbedMolecule(mol, randomSeed=0xf00d)
    descs = Descriptors3D.CalcMolDescriptors3D(mol)
    assert 'InertialShapeFactor' in descs
    assert 20.9582649071385 == pytest.approx(descs['PMI1'], 1e-4)


def test_data_dir_and_chemical_features():
    """Checks if data directory is correctly set
    and if ChemicalFeatures work
    """
    import os

    from rdkix import Chem, RDConfig
    from rdkix.Chem import ChemicalFeatures

    fdefName = os.path.join(RDConfig.RDDataDir, "BaseFeatures.fdef")
    factory = ChemicalFeatures.BuildFeatureFactory(fdefName)
    m = Chem.MolFromSmiles("OCc1ccccc1CN")
    feats = factory.GetFeaturesForMol(m)
    assert len(feats) == 8


def test_rdkix_chem_draw_import():
    # This segfaults if the compiled cairo version from centos is used
    from rdkix.Chem.Draw import ReactionToImage  # noqa: F401
