# class Segment:
#     def __init__(self, start_id: str, end_id: str, payload: str):
#         self.start_id = start_id
#         self.end_id = end_id
#         self.payload = payload

class Segment:
    def __init__(self, start_id, end_id, payload):
        self.start_id = start_id
        self.end_id = end_id
        self.payload = payload

segments = [
    Segment("AAA", "AAT", "AAAACGAAT"),
    Segment("GGT", "AAA", "GGTAAA"),
    Segment("AAT", "TGC", "AATCGTGC"),
    Segment("TGC", "CCT", "TGCAGCCT"),
    Segment("CCT", "TTT", "CCTGGTTT"),
    Segment("TTT", "GGA", "TTTAGGGA"),
]

"""
AAA -> AAT ->TGC ->CCT -> TTT -> GGA
    -> API
- reminds me of a graph 
{
    AAA: [(AAT, AAAACGAAT)]

}

"""

# example output -> GGTAAAACGAATCGTGCAGCCTGGTTTAGGGA

def reconstruct(segments: list[Segment]) -> str:
    """
    Reconstructs the full sequence from overlapping, ordered segments.
    """