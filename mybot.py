name: Deriv App ID Generation

on:
  pull_request:
    types: [opened, reopened, synchronize]

jobs:
  create-app-id:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Generate Deriv App ID
        id: deriv-app-id
        uses: ./.github/actions/deriv-app-id-action
        with:
          DERIV_API_TOKEN: ${{ secrets.DERIV_API_TOKEN }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          max_retries: 5

      - name: Output App ID
        run: echo "App ID: ${{ steps.deriv-app-id.outputs.app_id }}"
