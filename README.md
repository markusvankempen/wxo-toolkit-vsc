# WxO Toolkit — VS Code Extension (wxo-toolkit-vsc)

**IBM Watsonx Orchestrate**

*Author: Markus van Kempen · 27 Feb 2026*

**Repository:** [github.com/markusvankempen/wxo-toolkit-vsc](https://github.com/markusvankempen/wxo-toolkit-vsc)

Export, import, compare, and replicate Watson Orchestrate agents, tools, flows, and connections via the orchestrate CLI from VS Code. Uses wxo-toolkit-cli scripts bundled with the extension. Standalone extension (independent of wxo-builder).

## Features

- **Activity Bar** — Browse agents, tools, flows, connections with display names; inline actions (View JSON, Export, Copy, Edit, Compare, Delete)
- **Main Panel** — Export, Import, Compare, Replicate, Systems, Secrets, Dependencies, Help
- **Latest Report links** — Each tab shows a link to the most recent report (export, import, compare, replicate) with Refresh button
- **Create Tool** — Create Python or OpenAPI tools via form; outputs to `WxO/Exports/{env}/{datetime}/tools/{name}` (matches Export structure)
- **Import what** — Import all, agents only, tools only, flows only, or connections only
- **Systems** — Add, activate, remove Watson Orchestrate environments
- **Secrets** — Edit connection credentials per environment
- **WxO Project Dir** — Tree view of all subdirectories and files (Exports, Replicate, Compare, Systems)

## Usage

1. Open any workspace. The extension bundles the wxo-toolkit-cli scripts.
2. In the Activity Bar, click **WxO Toolkit** (↔ icon) → **Select Environment** to choose a Watson Orchestrate instance.
3. **Open Panel** to access Export, Import, Compare, Replicate, and more.
4. Use inline buttons on each resource for quick actions.

## Documentation

- **User Guide** — Run **WxO Toolkit: Open User Guide** from the Command Palette, or open the **Help** tab in the panel.
- Full guide: `USER_GUIDE.md` in this folder.

## Install from source

```bash
# Clone the repo (or use existing checkout)
git clone https://github.com/markusvankempen/wxo-toolkit-vsc.git
cd wxo-toolkit-vsc

npm install
npm run compile
```

Then in VS Code: **Run and Debug** → **Run Extension** (F5).

*When developing within the watson-orchestrate-builder monorepo, use `watsonx-orchestrate-devkit/packages/wxo-toolkit/vscode-extension` as the working directory.*

## Package for publishing

```bash
cd wxo-toolkit-vsc   # or watsonx-orchestrate-devkit/packages/wxo-toolkit/vscode-extension
npm run package
```

Produces `wxo-toolkit-vsc-1.0.0.vsix`. Install via **Extensions** → "..." → **Install from VSIX**.

See `PUBLISHING.md` for publishing to VS Code Marketplace and Open VSX.

### Files included in the VSIX

| File | Purpose |
|------|---------|
| `package.json` | Extension manifest |
| `dist/extension.js` | Bundled extension (esbuild) |
| `resources/*` | Icons, webview assets |
| `USER_GUIDE.md` | Full user guide (Help tab, Command Palette) |
| `SETUP.md` | Setup flow diagrams and detailed guide |
| `README.md` | Marketplace listing |

## Quick setup

1. **Add environment** — Open Panel → Systems tab → Add Environment (Name, URL, API Key)
2. Credentials are stored securely and synced to the orchestrate CLI
3. Export, Import, Compare, and Create Tool work immediately

See [SETUP.md](SETUP.md) for flow diagrams and a detailed guide.

## Using orchestrate in a Python venv

If you install the orchestrate CLI inside a Python virtual environment (e.g. `pip install ibm-watsonx-orchestrate` inside a venv), the extension needs to know where it is:

1. **Settings** → search `orchestrateVenvPath` (or **WxO Toolkit**)
2. Set **Orchestrate Venv Path** to your venv folder:
   - Workspace-relative: `.venv` or `venv` (if the venv is in your workspace root)
   - Absolute: `/path/to/your/venv`

The extension prepends `venv/bin` to `PATH` for all CLI operations. If you don't set this, Export/Import/Compare may fail with "orchestrate: command not found".

## Settings

| Setting | Description |
|---------|-------------|
| `wxo-toolkit-vsc.scriptsPath` | Path to wxo-toolkit-cli scripts folder. Leave empty to use bundled scripts. |
| `wxo-toolkit-vsc.wxoRoot` | WxO Project Dir (default: `{workspaceRoot}/WxO`) |
| `wxo-toolkit-vsc.orchestrateVenvPath` | Path to Python venv where orchestrate CLI is installed (e.g. `.venv`). **Required when orchestrate is in a venv** — see above. |
| `wxo-toolkit-vsc.debugPanel` | Write panel HTML to `.vscode/wxo-panel-debug.html` for debugging |
