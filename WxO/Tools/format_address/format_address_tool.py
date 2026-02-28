"""
Python tool that formats an address into a human-readable string.
Used by the Address Form agent to display collected address data.

Use format_address_tool.py (not format_address.py) to avoid module/package
name collision that causes: 'format_address' is not a package.
"""
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool()
def format_address(
    street: str = "",
    city: str = "",
    state: str = "",
    zip_code: str = "",
    country: str = "",
) -> str:
    """Format address components into a single mailing-format string.

    Args:
        street: Street address line
        city: City name
        state: State or province (optional)
        zip_code: ZIP or postal code (optional)
        country: Country name

    Returns:
        Formatted address string suitable for mailing labels.
    """
    parts = []
    if street:
        parts.append(street.strip())
    line2 = []
    if city:
        line2.append(city.strip())
    if state:
        line2.append(state.strip())
    if zip_code:
        line2.append(zip_code.strip())
    if line2:
        parts.append(", ".join(line2))
    if country:
        parts.append(country.strip())
    return "\n".join(parts) if parts else "No address provided."
