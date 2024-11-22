# Helm Merge-Values Plugin

## Overview

The Helm Merge-Values plugin enhances Helm's templating capabilities by allowing users to merge multiple values files and command-line overrides seamlessly. This functionality is particularly useful for managing complex configurations across various environments, enabling a more organized and efficient deployment process.

## Features

- **Merge Multiple Values Files**: Combine several YAML files containing Helm values into a single cohesive set.
- **Command-Line Overrides**: Apply specific value overrides directly via the command line, ensuring flexibility and precision.
- **Consistent Templating**: Utilizes Helm's native templating engine to ensure consistent and reliable rendering of Kubernetes manifests.

## Installation

To install the Helm Merge-Values plugin, execute the following command:

```bash
helm plugin install https://github.com/nomalord/helm-merge-values
```

## Usage

The basic syntax for using the plugin is specified in the [helm template documentation](https://helm.sh/docs/helm/helm_template/#helm)

**Example:**

To merge two values files and override a specific value via the command line:

```bash
helm merge-values -f values1.yaml -f values2.yaml --set image.tag=2.0.0
```

This command merges `values1.yaml` and `values2.yaml`, then sets the `image.tag` to `2.0.0`.

## How It Works

The plugin leverages Helm's `template` command to process and render templates using the merged values. By integrating directly with Helm's templating engine, it ensures that the rendered manifests are consistent with Helm's standard processing, providing a reliable and predictable output.

## Benefits

- **Simplified Configuration Management**: Easily manage and merge configurations across different environments or deployment scenarios.
- **Enhanced Flexibility**: Apply specific overrides without modifying the original values files, maintaining clean and maintainable configurations.
- **Seamless Integration**: Built to work seamlessly with Helm's existing commands and workflows, ensuring a smooth user experience.

## License

This project is licensed under the GPLv3 License. See the [LICENSE](https://github.com/nomalord/helm-merge-values/blob/master/LICENSE) file for details.

---

For more information and advanced usage, please refer to the [official Helm documentation](https://helm.sh/docs/). 