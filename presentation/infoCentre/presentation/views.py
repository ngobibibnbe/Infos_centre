from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Kibana_frame




template_name=""
views={
"END":"http://localhost:5601/goto/b1dbdcae0aea83df2feb9eeb0fc9e38e?embed=true",
"ENP": "http://localhost:5601/app/kibana#/visualize/edit/df91c0e0-a123-11ea-9ef1-e1012968d7dc?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-5y,to:now))&_a=(filters:!(),linked:!f,query:(language:kuery,query:''),uiState:(),vis:(aggs:!((enabled:!t,id:'1',params:(field:nombre_de_dossier),schema:metric,type:sum),(enabled:!t,id:'2',params:(drop_partials:!f,extended_bounds:(),field:'trunc(orchestra_dossier.date_creation)',interval:d,min_doc_count:1,scaleMetricValues:!f,timeRange:(from:now-1y,to:now),useNormalizedEsInterval:!t),schema:segment,type:date_histogram),(enabled:!t,id:'3',params:(field:nom.keyword,missingBucket:!f,missingBucketLabel:Missing,order:desc,orderBy:'1',otherBucket:!f,otherBucketLabel:Other,size:5),schema:group,type:terms)),params:(addLegend:!t,addTimeMarker:!f,addTooltip:!t,categoryAxes:!((id:CategoryAxis-1,labels:(filter:!t,show:!t,truncate:100),position:bottom,scale:(type:linear),show:!t,style:(),title:(),type:category)),dimensions:(series:!((accessor:1,aggType:terms,format:(id:terms,params:(id:string,missingBucketLabel:Missing,otherBucketLabel:Other,parsedUrl:(basePath:'',origin:'http:%2F%2Flocalhost:5601',pathname:%2Fapp%2Fkibana))),label:'nom.keyword:%20Descending',params:())),x:(accessor:0,aggType:date_histogram,format:(id:date,params:(pattern:YYYY-MM-DD)),label:'trunc(orchestra_dossier.date_creation)%20per%20day',params:(date:!t,format:YYYY-MM-DD,interval:P1D,intervalESUnit:d,intervalESValue:1)),y:!((accessor:2,aggType:sum,format:(id:number,params:(parsedUrl:(basePath:'',origin:'http:%2F%2Flocalhost:5601',pathname:%2Fapp%2Fkibana))),label:'Sum%20of%20nombre_de_dossier',params:()))),grid:(categoryLines:!f),labels:(),legendPosition:right,seriesParams:!((data:(id:'1',label:'Sum%20of%20nombre_de_dossier'),drawLinesBetweenPoints:!t,interpolate:linear,lineWidth:2,mode:stacked,show:!t,showCircles:!t,type:histogram,valueAxis:ValueAxis-1)),thresholdLine:(color:%23E7664C,show:!f,style:full,value:10,width:1),times:!(),type:area,valueAxes:!((id:ValueAxis-1,labels:(filter:!f,rotate:0,show:!t,truncate:100),name:LeftAxis-1,position:left,scale:(mode:normal,type:linear),show:!t,style:(),title:(text:'Sum%20of%20nombre_de_dossier'),type:value))),title:'Procedure:%20nombre%20de%20dossier%20par%20proc%C3%A9dures',type:area))"
}
def getVue(request,id):
    if request.user.is_authenticated:
        try:
            link=Kibana_frame.objects.get(code=id).link
        except Kibana_frame.DoesNotExist:
            raise Http404("ce Code d'analyse n'existe pas ")
        
        return render(request,'visualisations/index.html',{'link':link,'user':request.user})
    else:
        raise Http404("Vous n'êtes pas autorisé à rentrer ici")


        
    
