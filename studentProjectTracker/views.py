from django.shortcuts import render
from django.http import Http404
from django.template import TemplateDoesNotExist

def advance_table(request):
    return render(request, 'advance-table.html')

def alert(request):
    return render(request, 'alert.html')

def auth_forgot_password(request):
    return render(request, 'auth-forgot-password.html')

def auth_login(request):
    return render(request, 'auth-login.html')

def auth_register(request):
    return render(request, 'auth-register.html')

def auth_reset_password(request):
    return render(request, 'auth-reset-password.html')

def avatar(request):
    return render(request, 'avatar.html')

def badge(request):
    return render(request, 'badge.html')

def basic_form(request):
    return render(request, 'basic-form.html')

def basic_table(request):
    return render(request, 'basic-table.html')

def blank(request):
    return render(request, 'blank.html')

def blog(request):
    return render(request, 'blog.html')

def breadcrumb(request):
    return render(request, 'breadcrumb.html')

def buttons(request):
    return render(request, 'buttons.html')

def calendar(request):
    return render(request, 'calendar.html')

def card(request):
    return render(request, 'card.html')

def carousel(request):
    return render(request, 'carousel.html')

def chart_amchart(request):
    return render(request, 'chart-amchart.html')

def chart_apexchart(request):
    return render(request, 'chart-apexchart.html')

def chart_chartjs(request):
    return render(request, 'chart-chartjs.html')

def chart_echart(request):
    return render(request, 'chart-echart.html')

def chart_morris(request):
    return render(request, 'chart-morris.html')

def chart_sparkline(request):
    return render(request, 'chart-sparkline.html')

def chat(request):
    return render(request, 'chat.html')

def checkbox_and_radio(request):
    return render(request, 'checkbox-and-radio.html')

def collapse(request):
    return render(request, 'collapse.html')

def contact(request):
    return render(request, 'contact.html')

def create_post(request):
    return render(request, 'create-post.html')

def datatables(request):
    return render(request, 'datatables.html')

def dropdown(request):
    return render(request, 'dropdown.html')

def editable_table(request):
    return render(request, 'editable-table.html')

def email_compose(request):
    return render(request, 'email-compose.html')

def email_inbox(request):
    return render(request, 'email-inbox.html')

def email_read(request):
    return render(request, 'email-read.html')

def empty_state(request):
    return render(request, 'empty-state.html')

def errors_403(request):
    return render(request, 'errors-403.html')

def errors_404(request):
    return render(request, 'errors-404.html')

def errors_500(request):
    return render(request, 'errors-500.html')

def errors_503(request):
    return render(request, 'errors-503.html')

def export_table(request):
    return render(request, 'export-table.html')

def flags(request):
    return render(request, 'flags.html')

def form_wizard(request):
    return render(request, 'form-wizard.html')

def forms_advanced_form(request):
    return render(request, 'forms-advanced-form.html')

def forms_editor(request):
    return render(request, 'forms-editor.html')

def forms_validation(request):
    return render(request, 'forms-validation.html')

def gallery1(request):
    return render(request, 'gallery1.html')

def gmaps_advanced_route(request):
    return render(request, 'gmaps-advanced-route.html')

def gmaps_draggable_marker(request):
    return render(request, 'gmaps-draggable-marker.html')

def gmaps_geocoding(request):
    return render(request, 'gmaps-geocoding.html')

def gmaps_geolocation(request):
    return render(request, 'gmaps-geolocation.html')

def gmaps_marker(request):
    return render(request, 'gmaps-marker.html')

def gmaps_multiple_marker(request):
    return render(request, 'gmaps-multiple-marker.html')

def gmaps_route(request):
    return render(request, 'gmaps-route.html')

def gmaps_simple(request):
    return render(request, 'gmaps-simple.html')

def icon_feather(request):
    return render(request, 'icon-feather.html')

def icon_font_awesome(request):
    return render(request, 'icon-font-awesome.html')

def icon_ionicons(request):
    return render(request, 'icon-ionicons.html')

def icon_material(request):
    return render(request, 'icon-material.html')

def icon_weather_icon(request):
    return render(request, 'icon-weather-icon.html')

def index(request):
    return render(request, 'index.html')

def invoice(request):
    return render(request, 'invoice.html')

def light_gallery(request):
    return render(request, 'light-gallery.html')

def list_group(request):
    return render(request, 'list-group.html')

def mail_inbox(request):
    return render(request, 'mail-inbox.html')

def media_object(request):
    return render(request, 'media-object.html')

def modal(request):
    return render(request, 'modal.html')

def multiple_upload(request):
    return render(request, 'multiple-upload.html')

def navbar(request):
    return render(request, 'navbar.html')

def owl_carousel(request):
    return render(request, 'owl-carousel.html')

def pagination(request):
    return render(request, 'pagination.html')

def popover(request):
    return render(request, 'popover.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def posts(request):
    return render(request, 'posts.html')

def pricing(request):
    return render(request, 'pricing.html')

def profile(request):
    return render(request, 'profile.html')

def progress(request):
    return render(request, 'progress.html')

def subscribe(request):
    return render(request, 'subscribe.html')

def sweet_alert(request):
    return render(request, 'sweet-alert.html')

def tabs(request):
    return render(request, 'tabs.html')

def timeline(request):
    return render(request, 'timeline.html')

def toastr(request):
    return render(request, 'toastr.html')

def tooltip(request):
    return render(request, 'tooltip.html')

def typography(request):
    return render(request, 'typography.html')

def vector_map(request):
    return render(request, 'vector-map.html')

def widget_chart(request):
    return render(request, 'widget-chart.html')

def widget_data(request):
    return render(request, 'widget-data.html')

# def page(request, page):
#     if '..' in page or page.startswith('/'):
#         raise Http404()

#     template_name = f'{page}.html'
#     try:
#         return render(request, template_name)
#     except TemplateDoesNotExist:
#         raise Http404()
