function getCsrfToken() {
      return fetch('/api/csrf-token/')
          .then(response => response.json())
          .then(data => data.csrfToken);
  }