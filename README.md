# WxO Toolkit — VS Code Extension (wxo-toolkit-vsc)

**IBM Watsonx Orchestrate**

*Author: Markus van Kempen · 27 Feb 2026*

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
cd watsonx-orchestrate-devkit/packages/wxo-toolkit/vscode-extension
npm install
npm run compile
```

Then in VS Code: **Run and Debug** → **Run Extension** (F5).

## Package for publishing

```bash
cd watsonx-orchestrate-devkit/packages/wxo-toolkit/vscode-extension
npm run package
```

Produces `wxo-toolkit-vsc-1.0.0.vsix`. Install via **Extensions** → "..." → **Install from VSIX**.

See `PUBLISHING.md` for publishing to VS Code Marketplace and Open VSX.

## Settings

| Setting | Description |
|---------|-------------|
| `wxo-toolkit-vsc.scriptsPath` | Path to wxo-toolkit-cli scripts folder. Leave empty to use bundled scripts. |
| `wxo-toolkit-vsc.wxoRoot` | WxO Project Dir (default: `{workspaceRoot}/WxO`) |
| `wxo-toolkit-vsc.debugPanel` | Write panel HTML to `.vscode/wxo-panel-debug.html` for debugging |
