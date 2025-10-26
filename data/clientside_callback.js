    function (n_vertical, n_horizontal, n_radial, n_force) {
        const triggered = dash_clientside.callback_context.triggered[0];
        if (!triggered) return window.dash_clientside.no_update;

        const btnId = triggered.prop_id.split('.')[0];
        let options = {};

        switch(btnId) {
            case 'btn-vertical':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'DOWN',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100,
                    'n_vertical': n_vertical
                };
                break;
            case 'btn-horizontal':
                options = {
                    'elk.algorithm': 'layered',
                    'elk.direction': 'RIGHT',
                    'elk.spacing.nodeNode': 80,
                    'elk.layered.spacing.nodeNodeBetweenLayers': 100,
                    'n_vertical': n_vertical
                };
                break;
            case 'btn-radial':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.radial',
                    'elk.radial.radius': 200,
                    'n_vertical': n_vertical
                };
                break;
            case 'btn-force':
                options = {
                    'elk.algorithm': 'org.eclipse.elk.force',
                    'elk.force.iterations': 300,
                    'elk.spacing.nodeNode': 80,
                    'n_vertical': n_vertical
                };
                break;
            default:
                return window.dash_clientside.no_update;
        }
        return JSON.stringify(options);
    }