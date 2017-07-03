"""
拓扑，关联spout与bolt
"""

from streamparse import Grouping, Topology
from bolts.data_bolt import DataBolt
from spouts.data_spout import DataSpout


class WordCount(Topology):
    """
    关联spout与bolt
    """
    spout_spec = DataSpout.spec()
    bolt_spec = DataBolt.spec(
        inputs={spout_spec: Grouping.fields('message')},
        par=2
    )
