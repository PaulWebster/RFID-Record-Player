# Changelog

## Unreleased

### Added
- RFID tags detected without a mapping are saved to `rfid.json` and shown as unmapped in the web interface.
- Unmapped tags can be selected in the web interface to prefill the mapping form.
- RFID scanning now runs regardless of magnet detection; mapped tags only start playback when the magnet is detected.
- Activity log records unmapped tag discoveries and includes tag IDs when tags are added or removed.
- Mapped RFID tags can be edited by loading their current details into the web form.

### Changed
- Startup and installer messages now use the system hostname for the web interface URL.
- Web UI, firewall rules, setup examples, and documentation now use the port configured in `web_port.conf` (default: 8082).
- Runtime, setup, installer, and firewall configuration fall back to port 8080 when `web_port.conf` is missing, invalid, or unreadable.

### Fixed
- Interactive runs restore the terminal's original settings on shutdown to prevent it being left in no-echo mode.
