
# Helm Merge Values Plugin

The Helm Merge Values Plugin is a tool designed to streamline the process of combining multiple Helm values files and command-line overrides. This functionality is particularly useful for managing complex configurations across various environments, ensuring consistency and reducing redundancy.

## Features

- **Combine Multiple Values Files**: Merge several YAML files containing Helm values into a single cohesive configuration.
- **Incorporate Command-Line Overrides**: Apply `--set`, `--set-file`, and `--set-string` overrides during the merge process to customize configurations dynamically.
- **Maintain Helm's Merging Logic**: Utilizes Helm's native merging logic to ensure predictable and reliable outcomes.

## Installation

To install the Helm Merge Values Plugin, execute the following command:

```bash
helm plugin install https://github.com/nomalord/helm-merge-values.git
```

This command fetches and installs the plugin from the specified GitHub repository.

## Usage

After installation, you can use the plugin to merge values files and apply overrides. The basic syntax is:

```bash
helm merge-values [-f/--values path ...] [--set key=value,key=value ...] [--set-file key=path,key=path ...] [--set-string key=value,key=value ...]
```

**Example:**

To merge two values files and set an additional value:

```bash
helm merge-values -f values1.yaml -f values2.yaml --set image.tag=1.0.0
```

This command merges `values1.yaml` and `values2.yaml`, then sets the `image.tag` to `1.0.0`.

## Use Cases

- **Environment-Specific Configurations**: Manage different configurations for development, staging, and production environments by merging base values with environment-specific overrides.
- **Microservices Architecture**: Share common configurations across multiple services while allowing service-specific customizations.
- **Complex Deployments**: Simplify the management of intricate Helm deployments by consolidating configurations into a single, cohesive file.

## Contributing

Contributions to the Helm Merge Values Plugin are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Implement your changes and add tests as needed.
4. Submit a pull request with a detailed description of your changes.

Please ensure that your contributions adhere to the project's coding standards and include appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information and to access the source code, visit the [GitHub repository](https://github.com/nomalord/helm-merge-values). 