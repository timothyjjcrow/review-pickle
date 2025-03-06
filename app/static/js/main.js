/**
 * PicklePulse - Main JavaScript File
 */

document.addEventListener("DOMContentLoaded", function () {
  // Initialize Bootstrap tooltips
  var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });

  // Initialize Bootstrap popovers
  var popoverTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="popover"]')
  );
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
  });

  // Handle search form submission
  const searchForm = document.querySelector("form.d-flex");
  if (searchForm) {
    searchForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const searchInput = this.querySelector('input[type="search"]');
      const searchTerm = searchInput.value.trim();

      if (searchTerm) {
        window.location.href = `/reviews?search=${encodeURIComponent(
          searchTerm
        )}`;
      }
    });
  }

  // Handle filter form submissions
  const filterForm = document.querySelector(".filters-sidebar form");
  if (filterForm) {
    filterForm.addEventListener("submit", function (e) {
      e.preventDefault();

      // Build query string from form data
      const formData = new FormData(filterForm);
      const queryParams = new URLSearchParams();

      for (const [key, value] of formData.entries()) {
        if (value) {
          queryParams.append(key, value);
        }
      }

      // Redirect to filtered results
      window.location.href = `/reviews?${queryParams.toString()}`;
    });
  }

  // Handle sort select change
  const sortSelect = document.querySelector(".sort-select");
  if (sortSelect) {
    sortSelect.addEventListener("change", function () {
      // Get current URL and parameters
      const url = new URL(window.location.href);
      const params = url.searchParams;

      // Update sort parameter
      params.set("sort", this.value);

      // Redirect to sorted results
      window.location.href = `${url.pathname}?${params.toString()}`;
    });
  }

  // Activate the correct radio button based on URL parameters
  function activateCurrentFilters() {
    const url = new URL(window.location.href);
    const params = url.searchParams;

    // Handle category filter
    const category = params.get("category");
    if (category) {
      const categoryInput = document.querySelector(
        `input[name="category"][value="${category}"]`
      );
      if (categoryInput) {
        categoryInput.checked = true;
      }
    }

    // Handle price range filter
    const priceRange = params.get("price_range");
    if (priceRange) {
      const priceInput = document.querySelector(
        `input[name="price_range"][value="${priceRange}"]`
      );
      if (priceInput) {
        priceInput.checked = true;
      }
    }

    // Handle brand filter
    const brand = params.get("brand");
    if (brand) {
      const brandSelect = document.querySelector('select[name="brand"]');
      if (brandSelect) {
        brandSelect.value = brand;
      }
    }

    // Handle sort select
    const sort = params.get("sort");
    if (sort) {
      const sortSelect = document.querySelector(".sort-select");
      if (sortSelect) {
        sortSelect.value = sort;
      }
    }
  }

  // Call on page load
  activateCurrentFilters();

  // Add animation to cards
  const cards = document.querySelectorAll(".card");
  cards.forEach((card) => {
    card.classList.add("fade-in");
  });

  // Make external links open in new tab
  const externalLinks = document.querySelectorAll('a[href^="http"]');
  externalLinks.forEach((link) => {
    if (!link.getAttribute("target")) {
      link.setAttribute("target", "_blank");
      link.setAttribute("rel", "noopener noreferrer");
    }
  });

  console.log("PicklePulse JS initialized");
});
