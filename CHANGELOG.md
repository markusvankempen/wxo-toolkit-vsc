# Changelog

All notable changes to the WxO Toolkit VS Code extension ([wxo-toolkit-vsc](https://github.com/markusvankempen/wxo-toolkit-vsc)).

## [1.1.0] - 2026-02-25

### Added

- **Extension-first credentials** — API keys are stored in VS Code SecretStorage (encrypted). Add Environment in the Systems tab now syncs to orchestrate CLI and stores credentials securely.
- **Copy to .env** — New button in Systems tab to copy stored credentials to workspace `.env` (optional).
- **SETUP.md** — Setup guide with Mermaid flow diagrams for credentials flow, add environment, and script execution.
- **Credential merge** — Export, Import, Compare, Replicate, and Create Tool merge SecretStorage + `.env`; SecretStorage takes precedence.

### Changed

- **Add Environment** — API key is now recommended; when provided, credentials are saved to SecretStorage and `orchestrate env activate` is run so orchestrate config is populated.
- **WxOEnvironmentService** — `activateEnvironment` checks SecretStorage first, then `.env`.
- **Script execution** — Scripts receive a merged env file (SecretStorage + workspace `.env`) when credentials are in extension storage.
- **Documentation** — USER_GUIDE and README updated for the new flow; SETUP.md added with flow diagrams.

---

## [1.0.1] - 2026-02-25

### Added

- **Python venv documentation** — README, USER_GUIDE, Help tab, and Dependencies pane now explain how to set `orchestrateVenvPath` when orchestrate CLI is in a virtual environment
- **Marketplace discoverability** — Categories (Machine Learning, Data Science, Testing, Other), expanded keywords, and updated description for better findability on VS Code Marketplace and Open VSX

### Changed

- Improved `orchestrateVenvPath` setting description in Settings UI
- Enhanced USER_GUIDE with venv path examples table

### Fixed

- **Packaging** — Added tslib dependency and npm overrides so `npm run package` succeeds (vsce/@azure/identity requires tslib)

---

## [1.0.0] - 2026-02-27

### Added

- **Activity Bar view** — Browse agents, tools, flows, connections with display names
- **Main Panel** — Export, Import, Compare, Replicate, Systems, Secrets, Dependencies, Help tabs
- **Latest report links** — Export, Import, Compare, Replicate tabs show "Latest report: 📄 Open Report" with Refresh button
- **Create Tool form** — Create Python or OpenAPI tools; output to `WxO/Exports/{env}/{datetime}/tools/{name}` (matches Export structure)
- **Import what** — Choose to import all, agents only, tools only, flows only, or connections only
- **Display names** — Tools and flows show `display_name` in the Activity Bar (fallback to `name`)
- **WxO Project Dir tree** — Browse all subdirectories and files (depth 50)
- **Inline actions** — View JSON, Export, Copy, Edit, Compare, Delete on each resource
- **Systems management** — Add, activate, remove Watson Orchestrate environments
- **Secrets editor** — Edit connection credentials per environment
- **Bundled scripts** — wxo-toolkit-cli scripts included; optional `scriptsPath` override

### Configuration

- `wxo-toolkit-vsc.scriptsPath` — Path to wxo-toolkit-cli scripts (default: use bundled)
- `wxo-toolkit-vsc.wxoRoot` — WxO project root (default: `{workspaceRoot}/WxO`)
- `wxo-toolkit-vsc.debugPanel` — Write panel HTML for browser debugging
