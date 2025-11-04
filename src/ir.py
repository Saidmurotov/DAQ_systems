from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class ResourceType(str, Enum):
    ADC = "adc"
    TIMER = "timer"

@dataclass
class HardwareResource:
    """Represents a hardware resource such as an ADC or Timer."""
    id: str
    type: ResourceType
    channels: List[str] = field(default_factory=list)  # logical channels this resource can serve
    max_rate_hz: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ResourceMapping:
    """Mapping from logical channel name to hardware resource and index."""
    channel: str
    resource_type: ResourceType
    resource_id: str
    index: int  # e.g., ADC channel index or timer id
    annotations: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Channel:
    name: str
    type: str  # "analog" | "digital"
    sample_rate_hz: float
    format: str  # "int16", "float32", etc.
    annotations: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Sensor:
    name: str
    channel: str
    config: Dict[str, Any] = field(default_factory=dict)
    annotations: Dict[str, Any] = field(default_factory=dict)

@dataclass
class IR:
    target: str
    channels: List[Channel] = field(default_factory=list)
    sensors: List[Sensor] = field(default_factory=list)
    resources: List[HardwareResource] = field(default_factory=list)
    mappings: List[ResourceMapping] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def find_resource(self, resource_type: ResourceType, resource_id: Optional[str] = None) -> Optional[HardwareResource]:
        for r in self.resources:
            if r.type == resource_type and (resource_id is None or r.id == resource_id):
                return r
        return None

    def map_channel(self, channel_name: str) -> Optional[ResourceMapping]:
        for m in self.mappings:
            if m.channel == channel_name:
                return m
        return None
