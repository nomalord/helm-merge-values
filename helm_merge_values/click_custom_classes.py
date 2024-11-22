import click

class StringArrayParamType(click.ParamType):
    name = "string array"

    def convert(self, value, param, ctx):
        """
        Convert StringArray of to key value pairs
        Example:
        test="test", thingy=[]
        :param value:
        :param param:
        :param ctx:
        :return:
        """
        split_pairs_from_value = value.split(',')
        key_value_pairs = []
        for key_value in split_pairs_from_value:
            if key_value.find('=') == -1:
                raise click.BadParameter(
                    message=f'key: "{key_value}" has no value',
                    param=param,
                    ctx=ctx,
                )
            key, value = key_value.split('=')
            if ' ' in key:
                raise click.BadParameter(
                    message=f'key: "{key}" has space (helm doesn\'t support spaces in keys from CLI)',
                    param=param,
                    ctx=ctx,
                )

            key_value_pairs.append((key, value))
        return key_value_pairs


class OrderedParamsCommand(click.Command):
    _options = []

    def parse_args(self, ctx, args):
        parser = self.make_parser(ctx)
        opts, _, param_order = parser.parse_args(args=list(args))
        for param in param_order:
            type(self)._options.append((param, opts[param.name].pop(0)))

        return super().parse_args(ctx, args)

if __name__ == '__main__':
    string_array_param = StringArrayParamType()
    test = string_array_param.convert("test=test,hello= 0", None, None)
    print(test)