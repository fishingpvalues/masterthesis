"""
Module: explain.py
Description:
    Provides helper functions to generate detailed, human-readable string descriptions
    for various domain objects such as Resources, Orders, Features, and Process Executions.
    The module is designed to work with objects from the ofact.twin.state_model package.
    
Usage Example:
    from explain import get_process_description
    description = get_process_description(process_execution)
    print(description)
    
Author: Your Name
Date: YYYY-MM-DD
"""

import logging
from typing import Any

from ofact.twin.state_model.entities import (
    StationaryResource,
    NonStationaryResource,
    ActiveMovingResource,
    PassiveMovingResource,
)
from ofact.twin.state_model.sales import Order, Feature

# Set up module logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_resource_details(resource: Any) -> str:
    """
    Generates a detailed description for a resource.

    Args:
        resource: The resource instance or tuple containing the resource.

    Returns:
        A multi-line string with resource details.
    """
    # Ensure resource is not None and unpack if provided as a tuple.
    if resource is None:
        return "Resource Details: Not available"

    if isinstance(resource, tuple):
        resource = resource[0]

    lines = []
    lines.append("Resource Details:")
    lines.append(f"  Name: {getattr(resource, 'name', 'Unknown')}")
    lines.append(f"  Entity Type: {getattr(resource, 'entity_type', 'Unknown')}")
    lines.append(f"  Quality: {getattr(resource, 'quality', 'Unknown')}")
    lines.append(
        f"  Inspected Quality: {getattr(resource, 'inspected_quality', 'Unknown')}"
    )
    try:
        lines.append(f"  Position: {resource.get_position()}")
    except Exception:
        lines.append("  Position: Unknown")

    if isinstance(resource, StationaryResource):
        lines.append("  Type: StationaryResource")
        try:
            lines.append(f"  Plant: {resource.get_plant_name()}")
        except Exception:
            lines.append("  Plant: Unknown")
        try:
            lines.append(f"  Efficiency: {resource.get_efficiency_parameters()}")
        except Exception:
            lines.append("  Efficiency: Unknown")
        lines.append(f"  Entry Edge: {getattr(resource, 'entry_edge', 'Unknown')}")
        lines.append(f"  Exit Edge: {getattr(resource, 'exit_edge', 'Unknown')}")
    elif isinstance(resource, NonStationaryResource):
        lines.append("  Type: NonStationaryResource")
        lines.append(f"  Orientation: {getattr(resource, 'orientation', 'Unknown')}")
        lines.append(
            f"  Storage Places: {getattr(resource, 'storage_places', 'Unknown')}"
        )
    elif isinstance(resource, ActiveMovingResource):
        lines.append("  Type: ActiveMovingResource")
        lines.append(f"  Speed: {getattr(resource, 'speed', 'Unknown')}")
        lines.append(f"  Energy Level: {getattr(resource, 'energy_level', 'Unknown')}")
    elif isinstance(resource, PassiveMovingResource):
        lines.append("  Type: PassiveMovingResource")
    else:
        lines.append("  Type: Unknown")

    return "\n".join(lines)


def get_order_details(order: Any) -> str:
    """
    Generates a detailed description for an order.

    Args:
        order: The order instance expected to have attributes such as identification,
               customer, and delivery_date_planned.

    Returns:
        A multi-line string with order details.
    """
    if order is None:
        return "Order Details: Not available"

    lines = []
    lines.append("Order Details:")
    try:
        lines.append(f"  ID: {order.identification}")
    except AttributeError:
        lines.append("  ID: Unknown")
    if hasattr(order, "customer"):
        lines.append(f"  Customer: {order.customer}")
    if hasattr(order, "delivery_date_planned"):
        lines.append(f"  Planned Delivery Date: {order.delivery_date_planned}")

    return "\n".join(lines)


def get_feature_details(feature: Any) -> str:
    """
    Generates a detailed description for a feature.

    Args:
        feature: The feature instance expected to have attributes like name, price,
                 optionally feature_cluster and selection_probability_distribution.

    Returns:
        A multi-line string with feature details.
    """
    if feature is None:
        return "Feature Details: Not available"

    lines = []
    lines.append("Feature Details:")
    lines.append(f"  Name: {getattr(feature, 'name', 'Unknown')}")
    lines.append(f"  Price: {getattr(feature, 'price', 'Unknown')}")
    if hasattr(feature, "feature_cluster"):
        lines.append(f"  Feature Cluster: {feature.feature_cluster}")
    try:
        prob = feature.selection_probability_distribution.get_expected_value()
        lines.append(f"  Expected Selection Probability: {prob}")
    except Exception:
        lines.append("  Selection Probability: Unknown")

    return "\n".join(lines)


def get_process_description(process_execution: Any) -> str:
    """
    Generates a comprehensive description for a process execution.

    This includes details such as event type, process info, main resource details,
    origin, destination, order details, and any involved parts or resources.

    Args:
        process_execution: The process execution instance with expected attributes.

    Returns:
        A multi-line string describing the process execution.
    """
    if process_execution is None:
        return "Process Execution Details: Not available"

    lines = []
    lines.append("Process Execution Details:")
    lines.append(f"  Event Type: {getattr(process_execution, 'event_type', 'Unknown')}")
    lines.append(f"  Process: {getattr(process_execution.process, 'name', 'Unknown')}")
    lines.append(
        f"  Executed Start Time: {getattr(process_execution, 'executed_start_time', 'Unknown')}"
    )
    lines.append(
        f"  Executed End Time: {getattr(process_execution, 'executed_end_time', 'Unknown')}"
    )

    lines.append("  Main Resource:")
    main_resource_details = get_resource_details(
        getattr(process_execution, "main_resource", None)
    )
    for detail in main_resource_details.split("\n"):
        lines.append("    " + detail)

    lines.append(f"  Origin: {getattr(process_execution, 'origin', 'Unknown')}")
    lines.append(
        f"  Destination: {getattr(process_execution, 'destination', 'Unknown')}"
    )
    lines.append(
        f"  Resulting Quality: {getattr(process_execution, 'resulting_quality', 'Unknown')}"
    )

    lines.append("  Order:")
    order_details = get_order_details(getattr(process_execution, "order", None))
    for detail in order_details.split("\n"):
        lines.append("    " + detail)

    lines.append(
        f"  Source Application: {getattr(process_execution, 'source_application', 'Unknown')}"
    )
    lines.append(
        f"  Connected Process Execution: {getattr(process_execution, 'connected_process_execution', 'Unknown')}"
    )

    lines.append("  Parts Involved:")
    for part, node in getattr(process_execution, "parts_involved", []):
        if isinstance(part, Feature):
            part_info = get_feature_details(part)
            lines.append("    - Feature:")
            for info in part_info.split("\n"):
                lines.append("      " + info)
        else:
            lines.append(f"    - Part: {part}, Node: {node}")

    lines.append("  Resources Used:")
    for item in getattr(process_execution, "resources_used", []):
        if isinstance(item, tuple):
            resource = item[0]
            node = item[1] if len(item) > 1 else "Unknown Node"
            lines.append(f"    - Resource: {resource}, Node: {node}")
            resource_details = get_resource_details(resource)
            for detail in resource_details.split("\n"):
                lines.append("      " + detail)
        else:
            lines.append(f"    - Resource: {item}")
            resource_details = get_resource_details(item)
            for detail in resource_details.split("\n"):
                lines.append("      " + detail)

    return "\n".join(lines)


if __name__ == "__main__":
    # In production, it is recommended to import this module and use its functions.
    # For example usage and quick debugging, we attempt to load the dynamic model below.
    try:
        from ofact.planning_services.model_generation.persistence import (
            deserialize_state_model,
        )
        from pathlib import Path

        # Adjust the path as needed for your environment.
        dynamic_state_model_path = Path(
            r"D:\ofact-intern\projects\iot_factory\order_sim_iot.pkl"
        )
        dynm = deserialize_state_model(
            source_file_path=dynamic_state_model_path,
            persistence_format="pkl",
            dynamics=True,
            deserialization_required=True,
        )

        process_executions = dynm.get_process_executions_list()

        for process_execution in process_executions:
            description = get_process_description(process_execution)
            print(description)
            print("-" * 80)
    except ImportError as ie:
        logger.error("Failed to import dynamic model: %s", ie)
    except Exception as e:
        logger.error("Error while generating process descriptions: %s", e)
