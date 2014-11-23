/*global module:false*/
module.exports = function(grunt) {

grunt.initConfig({
    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    banner: '/*! <%= pkg.title || pkg.name %> - v<%= pkg.version %> - ' +
      '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
      '<%= pkg.homepage ? "* " + pkg.homepage + "\\n" : "" %>' +
      '* Copyright (c) <%= grunt.template.today("yyyy") %> <%= pkg.author.name %>;' +
      ' Licensed <%= _.pluck(pkg.licenses, "type").join(", ") %> */\n',
    // Task configuration.

    copy: {
        images: {
            expand: true,
            cwd: 'assets/images/',
            src: '**',
            dest: 'xchange/static/images/'
        },
        fonts: {
            expand: true,
            cwd: 'assets/fonts/',
            src: '**',
            dest: 'xchange/static/fonts/'
        }
    },
    less: {
      development: {
          options: {
              compress: false
          },
          files: {
              'xchange/static/css/style.css': 'assets/less/style.less'
          }
      }
    },
    cssmin: {
        options: {
            banner: '/*! <%= pkg.name %> v<%= pkg.version %>, <%= grunt.template.today("yyyy-mm-dd") %> */\n'
        },
        combine: {
            files: {
                'xchange/static/css/style.css': [
                    'xchange/static/css/style.css'
                ]
            }
        }
    },
    coffee: {
        compile: {
            expand: true,
            flatten: true,
            cwd: 'assets/coffee',
            src: ['**/*.coffee'],
            dest: 'xchange/static/js/',
            ext: '.js'
        }
    },
    concat: {
        options: {
        },
        js: {
            src: [
                'bower_components/jquery/dist/jquery.js',
                'bower_components/jqueryui/ui/core.js',
                'bower_components/jqueryui/ui/effect.js',
                'bower_components/jqueryui/ui/widget.js',
                'bower_components/jqueryui/ui/tabs.js',
                'bower_components/jqueryui/ui/menu.js',
                'bower_components/jqueryui/ui/position.js',
                'bower_components/jqueryui/ui/autocomplete.js',
                'bower_components/fancybox/source/jquery.fancybox.js',
                'bower_components/jquery-icheck/icheck.js',
                'bower_components/select2/select2.js',
                'bower_components/jquery-form/jquery.form.js',
                'bower_components/iosslider/_src/jquery.iosslider.min.js',
                'bower_components/bootstrap/js/transition.js',
                'bower_components/jquery.maskedinput/jquery.maskedinput.min.js',
                'xchange/static/js/parallax.js',
                'assets/js/script.js'
            ],
            dest: 'xchange/static/js/script.js'
        },
        ui: {
            src: [
                'bower_components/jqueryui/ui/core.js',
                'bower_components/jqueryui/ui/effect.js',
                'bower_components/jqueryui/ui/widget.js',
                'bower_components/jqueryui/ui/tabs.js',
            ],
            dest: 'xchange/static/js/jquery-ui.min.js'
        }
    },
    uglify: {
        options: {
            banner: '/*! <%= pkg.name %> v<%= pkg.version %>, <%= grunt.template.today("yyyy-mm-dd") %> */\n'
        },
        build: {
            src: 'xchange/static/js/script.js',
            dest: 'xchange/static/js/script.js'
        },
        pages: {
            expand: true,
            cwd: 'assets/js/pages/',
            src: '*.js',
            dest: 'xchange/static/js/'
        }
    },
    watch: {
        less: {
            files: 'assets/less/**/*.less',
            tasks: ['less', 'cssmin']
        },
        js: {
            files: 'assets/js/**/*.js',
            tasks: ['concat']
        },
        coffee: {
            files: 'assets/coffee/**/*.coffee',
            tasks: ['coffee', 'concat']
        },
        images: {
            files: 'assets/images/**/*',
            tasks: ['copy:images']
        }
    }
});

grunt.loadNpmTasks('grunt-contrib-watch');
grunt.loadNpmTasks('grunt-contrib-less');
grunt.loadNpmTasks('grunt-contrib-concat');
grunt.loadNpmTasks('grunt-contrib-uglify');
grunt.loadNpmTasks('grunt-contrib-cssmin');
grunt.loadNpmTasks('grunt-contrib-copy');
grunt.loadNpmTasks('grunt-contrib-coffee');


grunt.registerTask('default', ['copy', 'less', 'cssmin', 'coffee', 'concat', 'watch']);
grunt.registerTask('build',   ['copy', 'less', 'cssmin', 'coffee', 'concat', 'uglify']);

};

