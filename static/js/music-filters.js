// static/js/music-filters.js

class MusicFilters {
    constructor() {
        this.init();
    }

    init() {
        this.setupLiveSearch();
        this.setupGenreDropdown();
        this.setupFilterControls();
    }

    setupLiveSearch() {
        const searchInput = document.getElementById('live-search');
        if (!searchInput) return;

        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    this.submitForm();
                }, 500); // Debounce for 500ms
            }
        );
    }

    setupGenreDropdown() {
        const btn = document.getElementById('genre-dropdown-btn');
        const dropdown = document.getElementById('genre-dropdown');

        if (!btn || !dropdown) return;

        btn.addEventListener('click', () => {
            dropdown.classList.toggle('hidden');
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!btn.contains(e.target) && !dropdown.contains(e.target)) {
                dropdown.classList.add('hidden');
            }
        });

    }

    setupFilterControls() {
        // Auto-submit on dropdown changes
        const filterSelects = document.querySelectorAll('#filter-form select');
        filterSelects.forEach(select => {
            select.addEventListener('change', () => {
                this.submitForm();
            });
        });

        // Clear filters
        const clearBtn = document.getElementById('clear-filters');
        if (clearBtn) {
            clearBtn.addEventListener('click', () => {
                window.location.href = window.location.pathname;
            });
        }
    }

    submitForm() {
        const form = document.getElementById('filter-form');
        if (form) {
            form.submit();
        }
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new MusicFilters();
});