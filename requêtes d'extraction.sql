/********requête d'extraction des informations sur les procédures et les dossiers **/
select trunc (orchestra_dossier.date_creation),

		count (distinct orchestra_dossier.id ) as nombre_de_dossier,
        ORCHESTRA_MESSAGE_TYPE.MESSAGE_TYPE_CATEGORY,
        orchestra_process.nom,orchestra_process.id,
        min(jbpm4_hist_procinst.duration_/3600) as delais_le_plus_bas,
		max(jbpm4_hist_procinst.duration_/3600) as delai_le_plus_haut,
		webguce.core_good.GOOD_HS_CODE,
		webguce.core_good.GOOD_quantity,
		webguce.core_good.GOOD_weight,
		from( ((((orchestra_dossier   join (select id_,
        duration_ from jbpm4_hist_procinst where duration_ is not null) jbpm4_hist_procinst  on orchestra_dossier.bpm_id=jbpm4_hist_procinst.id_) 
		left join ORCHESTRA_MESSAGE on orchestra_message.dossier_id = orchestra_dossier.ID) 
		left join ORCHESTRA_MESSAGE_TYPE on orchestra_message.service_action= ORCHESTRA_MESSAGE_TYPE.message_type_id)
		left join orchestra_process on orchestra_dossier.process_id = orchestra_process.id )
		left join webguce.core_good on orchestra_dossier.NUMERO_DOSSIER  =webguce.core_good.RECORD_ID)
		group by trunc(orchestra_dossier.date_creation),
        ORCHESTRA_MESSAGE_TYPE.MESSAGE_TYPE_CATEGORY ,
		ORCHESTRA_PROCESS.nom,
        jbpm4_hist_procinst.quartile,
        webguce.core_good.GOOD_HS_CODE,
		webguce.core_good.GOOD_quantity,
		webguce.core_good.GOOD_weight,


/*ajouter :
-les durées des signatures (inclus le c CI)
-le nombre de dossier actif

**/

/***requête d'extraction des  délais des procédures (quartiles ,avg)***/
select jbpm4_hist_procinst.start_,jbpm4_hist_procinst.duration_/3600 as duration_,
		ORCHESTRA_CHARGER.CH_NAME as nom_chargeur,
		Orchestra_charger.ch_niu as NIU_chargeur,
		jbpm4_id_user.id_ as initialisateur_dossier,
		jbpm4_hist_procinst.quartile,ORCHESTRA_PROCESS.nom as nom_procedure
from (select id_,duration_,jbpm4_hist_procinst.start_,NTILE(4) OVER (ORDER BY jbpm4_hist_procinst.duration_ DESC) AS quartile from jbpm4_hist_procinst where duration_ is not null) jbpm4_hist_procinst join orchestra_dossier
 on orchestra_dossier.bpm_id=jbpm4_hist_procinst.id_ 
 join jbpm4_id_user  on    jbpm4_id_user.dbid_= orchestra_dossier.INITIALIZER
left join orchestra_charger on orchestra_charger.CH_CODE=orchestra_dossier.charger
		left join orchestra_process on orchestra_dossier.process_id = orchestra_process.id 


        
        /***requête d'extraction des informations sur les partenaires **/
select trunc(jbpm4_hist_task.create_),count (distinct jbpm4_hist_task.dbid_ ) as nombre_de_taches ,
avg(JBPM4_HIST_TASK.DURATION_) as duration_traitement,
        jbpm4_hist_task.assignee_,
		count (distinct orchestra_dossier.id ) as nombre_de_dossiers,
        ORCHESTRA_MESSAGE_TYPE.MESSAGE_TYPE_CATEGORY as etat_des_dossiers,
        ORCHESTRA_PROCESS.nom as procedure,orchestra_process.id,
		ORCHESTRA_CHARGER.CH_NAME as nom_chargeur,
		Orchestra_charger.ch_niu as NIU_chargeur,
		jbpm4_id_user.id_ as initialisateur_dossier,
		webguce.core_good.GOOD_HS_CODE,
		webguce.core_good.GOOD_quantity,
		webguce.core_good.GOOD_weight,
		jbpm4_hist_actinst.ACTIVITY_NAME_

		from ((((((((jbpm4_hist_task join jbpm4_hist_actinst on jbpm4_hist_task.dbid_=jbpm4_hist_actinst.HTASK_) join JBPM4_HIST_PROCINST on jbpm4_hist_actinst.HPROCI_=JBPM4_HIST_PROCINST.DBID_)
		join orchestra_dossier  on orchestra_dossier.bpm_id=jbpm4_hist_procinst.id_)
		join orchestra_process on orchestra_dossier.process_id = orchestra_process.id )
		join jbpm4_id_user  on    jbpm4_id_user.dbid_= orchestra_dossier.INITIALIZER)
		left join orchestra_charger on orchestra_charger.CH_CODE=orchestra_dossier.charger)
		left join ORCHESTRA_MESSAGE on orchestra_message.dossier_id = orchestra_dossier.ID)
		left join ORCHESTRA_MESSAGE_TYPE on orchestra_message.service_action= ORCHESTRA_MESSAGE_TYPE.message_type_id)
		left join webguce.core_good on orchestra_dossier.NUMERO_DOSSIER =webguce.core_good.RECORD_ID
		group by 
        trunc(jbpm4_hist_task.create_),
        jbpm4_hist_task.assignee_,
        ORCHESTRA_MESSAGE_TYPE.MESSAGE_TYPE_CATEGORY , 
		ORCHESTRA_PROCESS.nom,ORCHESTRA_PROCESS.id,

        orchestra_charger.ch_name,
        JBPM4_ID_USER.ID_,
        Orchestra_charger.ch_niu, 
        webguce.core_good.GOOD_HS_CODE,
        webguce.core_good.GOOD_quantity,
		webguce.core_good.GOOD_weight,
		jbpm4_hist_actinst.ACTIVITY_NAME_

