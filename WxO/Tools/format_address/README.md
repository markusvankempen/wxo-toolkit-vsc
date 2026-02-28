# format_address – Python Tool (Fixed)

Formats address components (street, city, state, zip, country) into a mailing-format string.

## Fix for module/package error

The tool previously failed with: `No module named 'format_address.format_address'; 'format_address' is not a package`.

**Cause:** When the Python file has the same name as the tool (`format_address.py`), the Watson Orchestrate runtime can misresolve the import.

**Fix:** Use `format_address_tool.py` so the module name (`format_address_tool`) differs from the tool name (`format_address`). Binding: `format_address_tool:format_address`.

## Re-import to TZ1 (fix source system)

To update TZ1 so future exports have the correct structure, use an already-fixed export dir:

```bash
./import_to_wxo.sh --env TZ1 --tools-only --tool format_address --base-dir WxO/Exports/TZ1/20260226_130835
```

## Manual import

```bash
cd WxO/Tools/format_address
orchestrate tools import -k python -p . -f format_address_tool.py -r requirements.txt
```
