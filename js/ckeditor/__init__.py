from fanstatic import Library, Resource

library = Library('ckeditor', 'resources')

ckeditor = Resource(library, 'ckeditor_source.js', minified='ckeditor.js')
