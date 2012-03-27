/**
 * 
 * This is an API explorer for tastypie
 * 
 * It relies on jQuery and underscore.js
 * 
 */

APIExplorer = null;
(function () { 
    
    var default_config = { 
        base_endpoint: '/api/v1/'
    };

    function Livingstone(config) { 
        var combined_config = default_config;
        _.each(config, function(value, key, config) { 
            combined_config[key] = config[key];
        });
        Livingstone.prototype.init(combined_config);
    }
    
    Livingstone.Models = {};
    Livingstone.Views = {};
    Livingstone.Originals = {};

    Livingstone.Models.Application = function(label, end_point) { 
        this.label = label; this.end_point = end_point;
    };

    Livingstone.Views.APIView = function(data) { 
        this.template = '#endpoint-panel-template';
        this.data=data;
    };

    Livingstone.prototype = { 

        Applications: {}, 
        
        template: "#explorer-template",
        
        init: function(config) { 
            _.bindAll(this);
            this.$el = $(config['element']);
            this.options = config;
            var t = this;
            this.get_application_list(function() {
                t.render();
                Livingstone.Originals['endpoint-panel'] = 
                                        $("#endpoint-panel").html();

                Livingstone.Originals['schema-display'] = 
                                        $("#schema-display").html();
            });
        },

        get_application_list: function(callback) { 
            var t= this;
            $.get(this.options['base_endpoint'], function(response) { 
                _.each(response.objects, function(v,k,l) { 
                    t.Applications[v.application] = v.uri;
                });
                if (callback !== null && 
                    typeof callback == 'function') {  
                    callback();
                }
            });
        },

        get_application_api: function(app_url, callback) { 
            var t = this;
            $.get(app_url, function (response) { 
                if (typeof callback == 'function') { 
                    callback(response);
                }
            });
        },

        show_schema: function(api_data) { 
            $("#endpoint-panel").html(
                _.template($('#endpoint-panel-template').html(), 
                {schema:api_data}));
            
        },

        show_model_list: function(api_data) { 
            var t = this;
            $("#schema-display").html(
                _.template(
                    $("#schema-display-template").html(),
                    {
                        models: api_data
                    }
                )); 

            $("#endpoint-panel").html(
                Livingstone.Originals['endpoint-panel']);

            $("#schema-display a").click(function(evt) { 
                var schema_url = $(this).attr('href').substr(1);
                t.get_application_api(schema_url, t.show_schema);
            });
        },

        render: function() { 
            var t = this;
            this.$el.append (  
                _.template($(this.template).html(), 
                { 
                    applications: this.Applications,
                    appkeys: _.sortBy(
                                _.keys(this.Applications), 
                                function(key) { return key; }
                            )
                }));

            $("#application-list a").click(function(evt) { 
                var app_url = $(this).attr('href').substr(1);
                t.get_application_api(app_url, t.show_model_list);

                $("#endpoint-panel").html(
                    Livingstone.Originals['endpoint-panel']);

            });
        }
    };
     
    APIExplorer = Livingstone;

})();
