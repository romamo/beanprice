# Changelog

## Unreleased

### Fixed
- `--update-fill-gaps` no longer refetches past dates a source has no price for.
  `is_price_cache_skip` keyed the cache by the source module while fetches key it
  by the Source instance, so it never matched; both now use the module name
- A date at least 7 days old is settled: its cache entries never expire, and a
  fetch error on it, repeated on 2 separate days, is cached as a skip. A single
  error is still never cached as a skip (#4)

---

## [2.1.1] - 2026-03-31

### Fixed
- Merge all source files into a single in-memory ledger before generating price
  jobs, so commodity directives and existing price history is visible across
  files; eliminates duplicate jobs and missed cross-file declarations for both
  the `--update` and plain-file paths.

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
