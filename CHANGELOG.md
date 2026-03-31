# Changelog

## Unreleased

### Added
- Added Financial Times price source
- Added Yahoo Finance index support
- Added `--update-fill-gaps` to backfill missing price history
- Added streaming output so fetched prices are written immediately
- Added documentation for streaming output and backfill workflow
- Added cache-skip handling to avoid re-fetching no-value or clobbered prices
- Added Yahoo SSL retry with exponential backoff

### Changed
- Improved cache handling for missing prices
- Switched from collect-all-then-print to per-entry output flushing for crash safety
- Improved clobbered-entry handling in the main flow
- Added defensive handling for missing commodity directives in the inactive path
- Added debug logging in the lifetime trimming pipeline
