from .properties import ProteinProperties
from .heavy_chain import HeavyChain as HC
from .light_chain import LightChain as LC


class Mab:
    """
    A class representing a monoclonal antibody (mAb) object consisting of heavy chains (HC1, HC2),
    light chains (LC1, LC2), and Fab domains (Fab1, Fab2).

    Attributes:
        hc1 (HC): Heavy chain 1 object.
        hc2 (HC): Heavy chain 2 object.
        lc1 (LC): Light chain 1 object.
        lc2 (LC): Light chain 2 object.
        fab1 (_Fab): Fab domain 1 object.
        fab2 (_Fab): Fab domain 2 object.
        properties (ProteinProperties): Protein properties of the mAb.
    """

    def __init__(self, hc1_aa_sequence: str = None, hc2_aa_sequence: str = None,
                 lc1_aa_sequence: str = None, lc2_aa_sequence: str = None) -> None:
        """
        Initialize the Mab object with heavy and light chain sequences.

        Args:
            hc1_aa_sequence (str): Amino acid sequence of heavy chain 1.
            hc2_aa_sequence (str): Amino acid sequence of heavy chain 2.
            lc1_aa_sequence (str): Amino acid sequence of light chain 1.
            lc2_aa_sequence (str): Amino acid sequence of light chain 2.
        """
        self.hc1 = HC(hc1_aa_sequence) if hc1_aa_sequence else None
        self.lc1 = LC(lc1_aa_sequence) if lc1_aa_sequence else None
        self.hc2 = HC(hc2_aa_sequence) if hc2_aa_sequence else None
        self.lc2 = LC(lc2_aa_sequence) if lc2_aa_sequence else None
        self.fab1 = self._Fab(self.hc1, self.lc1) if self.hc1 and self.lc1 else None
        self.fab2 = self._Fab(self.hc2, self.lc2) if self.hc2 and self.lc2 else None
        self.properties = self._calculate_mab_properties([
            self.hc1.full_chain.sequence if self.hc1 else None,
            self.hc2.full_chain.sequence if self.hc2 else None,
            self.lc1.full_chain.sequence if self.lc1 else None,
            self.lc2.full_chain.sequence if self.lc2 else None
        ])

    def _calculate_mab_properties(self, chain_list: list[str]) -> ProteinProperties:
        """
        Calculate protein properties of the mAb domains.

        Args:
            chain_list (list[str]): List of amino acid sequences of mAb chains.

        Returns:
            ProteinProperties: Protein properties object.
        """
        if not chain_list or None in chain_list:
            return None
        return ProteinProperties(chain_list)

    class _Fab:
        """
        A class representing a Fab domain consisting of fd_sequence, lc_sequence, and properties.

        Attributes:
            fd_sequence (str): Amino acid sequence of the fd domain.
            lc_sequence (str): Amino acid sequence of the light chain domain.
            properties (ProteinProperties): Protein properties of the Fab domain.
        """

        def __init__(self, hc_obj: HC = None, lc_obj: LC = None) -> None:
            """
            Initialize the _Fab object with heavy and light chain objects.

            Args:
                hc_obj (HC): Heavy chain object.
                lc_obj (LC): Light chain object.
            """
            self.fd_sequence = hc_obj.fd.sequence if hc_obj else None
            self.lc_sequence = lc_obj.full_chain.sequence if lc_obj else None
            self.properties = self._calculate_fab_properties(self.fd_sequence, self.lc_sequence) \
                if self.fd_sequence and self.lc_sequence else None

        def _calculate_fab_properties(self, fd_seq: str, lc_seq: str) -> ProteinProperties:
            """
            Calculate protein properties of the Fab domains.

            Args:
                fd_seq (str): Amino acid sequence of the fd domain.
                lc_seq (str): Amino acid sequence of the light chain domain.

            Returns:
                ProteinProperties: Protein properties object.
            """
            if not fd_seq or not lc_seq:
                return None
            return ProteinProperties([fd_seq + lc_seq])






